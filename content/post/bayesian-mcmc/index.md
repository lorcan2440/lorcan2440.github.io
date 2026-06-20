---

title: "Understanding Bayesian Phylogenetics"
subtitle: Building up Bayesian inference and MCMC from first principles
date:
summary:
draft: false
featured: false
tags:
  - statistics
  - biology
categories: []

image:
    preview_only: true
    filename: featured.jpg

commentable: true

---

# Introduction

Bayesian phylogenetics is a powerful framework for inferring evolutionary relationships among species using probabilistic models. However, it can seem like a black box due to the complexity of the underlying mathematics and algorithms. After studying the raw theory of MCMC and Bayesian phylogenetics in depth for a few weeks, including reading Chapter 13 of Wheeler's textbook *Systematics*, seeing the derivations of every formula for myself, and coding my own MCMC program from scratch, I felt like I truly grasped the power of these techniques.

I wanted to provide a comprehensive explanation of these concepts, building up from first principles to the application in phylogenetics. This post will be purely theoretical and seeming irrelevant at first, then working up towards Bayesian phylogenetics (the same order in which I learned the topic).

# The Pure Mathematics Bits

## Statistical Distributions and Random Variables

Let's introduce what a *statistical distribution* is. If we roll a fair dice repeatedly, it will land on each number 1, 2, 3, 4, 5, 6 equally frequently. We say that the outcome of the dice roll (which we could denote as a discrete random variable $ X $) has a *uniform distribution*. If we calculate the proportion $ p $ of rolls that have a given outcome $ x $, we would find they all eventually converge to 1 in 6, or about 16.67%. We can plot this distribution $ p(x) $ on a graph:

[graph showing line graph of uniform distribution of a fair die]

Mathematically, we summarise this graph of the uniform distribution as

$$ p(x) = \frac{1}{6} \text{ for all } x \text{ in } \{1, 2, 3, 4, 5, 6\}. $$

Intuitively, the uniform distribution is what people mean when they say "random" in everyday life, but not all random variables (RVs) are uniformly distributed. For example, if the die is weighted on the 6 face, it will be more likely to land on 6 than any other number, so the distribution changes. If we graph the number of outcomes of each face against the face value (1-6), the bar chart (and hence the function $ p(x) $) will be lopsided towards 6.

[image showing a line graph of a weighted die distribution]

The above is an example of a discrete RV, but RVs can be continuous too. The height of adult humans on earth is a continuous RV, whose distribution can be described using some $ p(x) $, where $ x $ is the height of a human and $ p(x) $ is the frequency density at that height, which looks something like this:

[graph showing normal distribution of human heights]

In the continuous case, we refer to $ p(x) $ as the probability density function (PDF) of $ X $. The PDF is defined such that the probability of observing some outcome in the range between $ a $ and $ b $ is calculated by integrating $ p(x) $ with respect to $ x $ between $ a $ and $ b $:

$$ P(a \leq X \leq b) = \int_a^b p(x) \ \textrm{d}x. $$

## Sampling from Unknown Distributions

We would like to simulate obtaining samples from a distribution $ p(x) $. If we know the function $ p(x) $ we're aiming for, then there are relatively simple ways to generate samples from it, if we have access to a 'random number generator' (which generates uniform random numbers between 0 and 1).

However, in many cases, we don't know how to evaluate $ p(x) $ directly, but we do know that it is proportional to some other function $ f(x) $ that we *can* evaluate. In this case, we write

$$ p(x) = \frac{f(x)}{C}, $$

where $ C $ is a constant. This may seem like a very artificial case and an esoteric thing to want to do, but we will see that it is the backbone of an extremely powerful and general technique called the Metropolis-Hastings algorithm.

So, to summarise, what we're working towards first is:

{{% callout note %}}
**Goal of the Metropolis-Hastings Algorithm**: Generate samples of the RV $ X \sim p(x) $, where $$ p(x) = \frac{f(x)}{C} $$ and $ f(x) $ is **known**, but the constant $ C $ and $ p(x) $ are unknown.
{{% /callout %}}

## Markov Chains and Stationary Distributions

A Markov chain is a sequence of random variables $ X_1, X_2, X_3, \dots $ where the distribution of each variable depends only on the value of the previous variable. In other words, the next state only depends on the present state. This property is known as the **Markov property**.

There are two ways of thinking about Markov chains, depending on whether the state space (values of $ X $) is discrete or continuous. In the discrete case, we can represent the transition probabilities between states using a **transition matrix** $ P $, where each entry $ P_{ab} $ represents the probability of transitioning from state $ x_{n} = a $ to state $ x_{n+1} = b $. In the continuous case, we use a **transition kernel** $ T(a \rightarrow b) $, which gives the probability density function of transitioning to state $ x_{n+1} = b $ given that we are currently in state $ x_{n} = a $. We'll focus on the continuous case, as it is more general and applicable to our interests here.

The **stationary distribution** of a Markov chain is a distribution $ p(x) $ that remains unchanged under the transition dynamics of the chain. It is the distribution we converge to after we have stepped through the chain many times (in the limit of infinite steps, ideally). Mathematically, this can be expressed as:

{{% callout note %}}
**Detailed Balance Criterion**: If the transition probabilities in a Markov chain obey the criterion 
$$ \frac{T(a \rightarrow b)}{T(b \rightarrow a)} = \frac{p(b)}{p(a)} \text{ for all } a, b $$
then $ p(x) $ is the **stationary distribution** of the Markov chain.
{{% /callout %}}

The Metropolis-Hastings algorithm essentially constructs a Markov chain whose stationary distribution is the target distribution $ p(x) $, by choosing a carefully designed transition kernel $ T(a \rightarrow b) $. That way, by traversing this chain for a long time, we can obtain samples that are approximately distributed according to $ p(x) $ (our goal).

## Metropolis-Hastings Algorithm

We're now ready to describe how the Metropolis-Hastings algorithm works.

We start by defining a **proposal distribution** $ q(b | a) $, which can be any distribution that is easy to sample from. A common choice is the normal distribution with mean $ a $ and some fixed variance $ \sigma^2 $, so that the next proposed state is

$$ b \sim \mathcal{N}(a, \sigma^2). $$

This choice of $ q(b | a) $ means our next proposal $ b $ will usually be "nearby" to $ a $ (i.e. within a standard deviation $ \sigma $), but occasionally it will be further away, allowing us to explore the state space. 

(Side note on terminology: since this choice of $ q(b | a) $ is symmetric (i.e. $ q(b | a) = q(a | b) $), running with this proposal distribution is called the **Metropolis algorithm**, which is a special case of the more general Metropolis-Hastings algorithm where $ q(b | a) $ is not necessarily symmetric.)

Once we have decided on a proposal distribution $ q(b | a) $, we can start traversing the Markov chain. We begin at some initial state $ x_0 $, and then for each step $ n $, we:

1. Sample a new proposal $ b \sim q(b | a) $, where $ a $ is the most recently accepted state. In the first iteration, $ a = x_0 $.

2. Compute the **acceptance probability** $ A = A(b | a) $:

$$ A(b | a) = \min\left(1, \frac{f(b) \ q(a | b)}{f(a) \ q(b | a)}\right). $$

3. With probability $ A $, we *accept* the proposal and set $ x_{n+1} = b $. Otherwise (i.e. with probability $ 1 - A $), we *reject* the proposal and set $ x_{n+1} = a $ (we stay in the same state).

4. Repeat steps 1-3 for a large number of iterations $ N $ to generate a sequence of samples $ x_1, x_2, \dots, x_N $.

The acceptance probability formula $ A(b | a) $ is derived from the detailed balance criterion, and is what ensures that the stationary distribution of the Markov chain is $ p(x) $.

In theory, that's it! In practice, there are two nuances to be aware of:

1. **Burn-in**: The first few samples of the chain may not be representative of the stationary distribution, as the chain may still be "finding its way" to the high-probability regions of $ p(x) $. Therefore, we often discard the first $ M $ samples (the "burn-in" period) and only keep the subsequent samples for analysis, representative of stationarity. There are methods of determining a suitable value of $ M $ (e.g. using the integrated autocorrelation time), but a common heuristic is to discard the first 10-20% of samples.

2. **Autocorrelation**: The samples generated by the Markov chain are not independent, as each sample depends on the previous one by its design. Whether or not this is a problem depends on the application, but in general, it is preferable to have approximately independent (less correlated) samples. To mitigate this, we can "prune" the chain by only keeping every $ k $-th sample (e.g., every 10th sample), which reduces autocorrelation at the cost of discarding some data.

With these corrections, we now have a set of samples $ x_i $ that are approximately distributed according to $ p(x) $. We have achieved our goal!

## Monte Carlo Estimation

To recap, what we have so far with Metropolis-Hastings is a machine that takes in a function $ f(x) $ that we know how to evaluate, and spits out $ N $ representative samples $ x_i $ from its normalised distribution $ p(x) = \frac{f(x)}{C} $, where $ C $ is an unknown constant.

What can we do with these samples $ x_i $? We can now approximate practically any property of the random variable $ X \sim p(x) $ we need - such as the **mean** of $ X $, given by the expectation

$$ \text{E}[X] = \int_{-\infty}^{\infty} x \ p(x) \ \textrm{d}x \approx \bar{x} = \frac{1}{N} \sum_{i=1}^N x_i $$

The right-hand side expression is the **Monte Carlo estimate** of the expectation, which is simply the average of the samples $ x_i $. Computing the nasty integral on the left-hand side has been reduced to adding up some numbers! That's because the hard work was already done by the Markov chain step, which ensures the distribution of those numbers matches $ p(x) $.

Other properties of $ X $ can also be estimated, such as:

- The **mode** of $ X $, i.e. the maximum point of $ p(x) $, which can be approximated by evaluating $ f(x_i) $ for all of our samples and then finding $ x^* = \arg \max f(x) $.
- The **median** of $ X $, which can be approximated by sorting the samples $ x_i $ and taking the middle value.

More generally, we can estimate the expectation of any function $ g(X) $ of the random variable $ X $:

$$ \text{E}[g(X)] = \int g(x) \ p(x) \ \textrm{d}x \approx \frac{1}{N} \sum_{i=1}^N g(x_i) $$

This formula can be used to estimate the **variance** of $ X $ by taking $ g(X) = (X - \text{E}[X])^2 $.

These quantities are the main outputs of MCMC methods, and they are the quantities we will be interested in when we apply MCMC to Bayesian phylogenetics.

## Bayesian Inference using MCMC

Given data $D$, a model (hypothesis) $\theta$, and a way of computing likelihoods $p(D | \theta)$, we aim to sample from the posterior probability distribution

$$ p(\theta | D) = \frac{p(D | \theta) p(\theta)}{p(D)} $$

where

$$ p(D) = \int p(D, \theta) \ d\theta $$

is the marginal likelihood (or evidence), and $p(\theta)$ is the prior distribution of the model parameters. The challenge is that $p(D)$ is often difficult to compute directly, but we can use MCMC methods to sample from the posterior distribution without needing to calculate it explicitly.

If $ \theta $ is in a high-dimensional state space (many model parameters), then computing $ p(D) $ by integration is computationally intractable. However, we can treat  $ f(\theta) = p(\theta, D)  $ as an unnormalised distribution, proportional to $p(\theta | D)$ with normalising constant $C = p(D)$.

By applying the Metropolis-Hastings algorithm to $ f(\theta) $, using Bayes’ theorem to write  $ f(\theta) = p(D | \theta) p(\theta) $,  where $ p(\theta) $ is a suitable prior distribution, and $ p(D | \theta) $ is computable, we can obtain samples of 
$ \theta_n \sim p(\theta | D) $. The acceptance probability of each new proposal $ \theta' \sim q(\theta' | \theta) $ is:

$$ A(\theta' | \theta) = \min\left(1, \frac{p(D | \theta') \ p(\theta') \ q(\theta | \theta')}{p(D | \theta) \ p(\theta) \ q(\theta' | \theta)}\right) $$

Monte Carlo estimation can then be applied as usual to the stationary model parameter samples $\theta_n$.

## Simulated Annealing

If the objective is to find $ x^* = \arg\max p(x) $ (optimisation) rather than sampling from $p$, then we can effectively sample from $f(x)^\beta$ in the limit as $\beta \to \infty$ instead (smaller values vanish). This is achieved (for symmetric proposal distributions $q$) by modifying the Metropolis acceptance probability expression to

$$ A(b | a) = \exp \left(  \frac{\Delta E}{T} \right) \ \ \ \text{where} \ \ \ \Delta E = f(b) - f(a) \ \ \text{and} \ \ T = \frac{1}{\beta}. $$

Here, $T$ is the chain's **temperature** parameter, and $\Delta E = f(b) - f(a)$ is the change in the objective function. By gradually lowering $T$ (**annealing**), we can explore the state space more freely at high temperatures and focus on high-probability regions at low temperatures, allowing us to find global maxima. The accepted samples converge towards optimality $ x^* $ as the temperature $ T \to 0 $.

An **annealing schedule** is a procedure for slowly decrementing $ T $ over time. It is intended to balance between exploration (accepting worse solutions to escape local maxima) and exploitation (narrowing in on the highest found maximum). Standard annealing schedules include geometric ($ T_n = T_0 \alpha^n, 0 < \alpha < 1$), logarithmic ($ T_n = T_0 / \ln(e + n) $) and adaptive (Cauchy) ($ T_n = g(T_{n-1}, \Delta E_{n-1}) $: ‘reheating’ allowed).

SA is a ‘meta-heuristic algorithm’: it is theoretically guaranteed to find the global optimum after infinite time, but in practice, running SA for finite time only gives an estimate for $x^*$, and it may still get stuck at a local maximum.

When used in Bayesian MCMC, SA finds the **maximum a posteriori** (MAP) estimate. If the prior is also uniform, then this is also the **maximum likelihood** (ML) estimate (the peak of $p(\theta | D)$).

Note that SA is not limited to functions $ p(x) $ that are probability measures: it is applicable to any function.

## Metropolis-Coupled MCMC (MC$^3$)

A combination of MCMC with SA is called **Metropolis-coupled MCMC** (abbreviated MC$^3$), aka 'parallel tempering'.

The temperature-based acceptance probability rule from SA is used in the Metropolis algorithm, but with several Markov chains all iterating independently at the same time. The chains are initialised at different temperatures to represent different tempered distributions:

$$ p_{\beta}(x) = \frac{f(x)^\beta}{C(\beta)} $$ 

(recall $ \beta $ is the 'inverse temperature': $ \beta = 1 / T $). The heated chains ($T > 1$) traverse a smoothened landscape, while the cold chain ($T = 1$) tracks maxima frequently as usual.

Periodically, the algorithm proposes a swap of states between two chains, helping to escape local maxima on the cold chain. More frequent swapping reduces autocorrelation in the chains. Following burn-in, the WSS samples from only the coldest chain are returned as representing $ p(x) $.

MC$^3$ can be efficiently implemented computationally using multiprocessing, in which each chain is run on a separate CPU core. This is a form of parallel computing.

In addition to being more robust and more exploratory than standard MCMC, MC$^3$ also comes with the perk of being able to estimate the normalising constant $ C $, which is the marginal likelihood $ C = p(D) $ in Bayesian MCMC. This is something that is tricky to do in standard MCMC. In MC$^3$, this is done by **thermodynamic integration**: we obtain stationary samples from all chains and compute $ \text{E}[\ln f(X)] $ for each chain using Monte Carlo. Then, using numerical integration (e.g. Riemann summation), estimate $ C $ by integrating over all $ \beta $:

$$ \ln C = \int_0^1 \text{E}_{\beta}[\ln f(X)] \ d\beta. $$

In Bayesian MCMC, $ C = p(D) $ can be used to estimate Bayes factors:

$$ \text{BF}_{12} = \frac{p(D | \theta_1)}{p(D | \theta_2)} = \frac{C_1}{C_2} $$

where $\theta_1$ and $\theta_2$ are the parameters of two competing models. This is a powerful tool for model comparison in Bayesian statistics.

---

# The Biology Bits

## Models of Mutation Rates

## Permutations in Tree State Space

## Bayesian Phylogenetics

---