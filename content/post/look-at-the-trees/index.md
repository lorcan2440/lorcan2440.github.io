---

title: "Look at the trees! Evolution and engineering in action"
subtitle: A short essay on trees from an engineering perspective, and its implications for evolution and design
date:
summary:
draft: true
featured: true
tags:
  - biology
  - evolution
categories: []

image:
    preview_only: true
    filename: featured.jpg

commentable: true

---

I don't have a good intro to this post, it comes from a bit of wikipedia rabbit-hole-diving I did while brushing up on the theory of buckling in columnar structures for work. It started with some curious fun facts about the way trees grow and ended up revealing many interconnected threads that demonstrate the power of evolution. [Consilience](https://www.facebook.com/groups/evolutionx/posts/1354749152309000/) (convergence of independent lines of evidence on a singular conclusion) tends to do that, of course.

Writeup for reddit: [here](https://www.reddit.com/r/DebateEvolution/comments/1pwj75f/comment/nw56let/) (modified for blog format).

## *Why* do trees grow tall?

Plants have embarked on the thermodynamically-Sisyphean task of getting carbon dioxide to do stuff for them, rolling carbon-containing molecules up the Gibbs free energy mountain (the Calvin cycle of photosynthesis) to make food molecules (glucose and carbs) which release the energy back to them (respiration), before starting over. In human-centric life, we think of CO2 as a waste product that's good for nothing except anthropogenic global warming*. Plants get away with using CO2 as their input because they have the Sun, beaming in limitless free energy to a planet that would otherwise be lifeless.

\* *oops, I lost half the creationist readers with that one already...*

Of course, it wasn't plants who came up with this trick. That goes back to the original photosynthetic microorganisms, a phylum of prokaryotes called cyanobacteria. Protists, like the ancestors of algae, just took control of this mini-generator and put it into an organelle (endosymbiosis) that we now call the chloroplast. Once multicellular, plant evolution was guided by one rule: more sunlight → more energy → more growth → more sunlight. Since more growth also comes with more reproduction via further seed dispersal and germination, this positive feedback became subject to natural selection.

Problem: trees don't grow in a vacuum (duh, they need air). When seeds fall to land, they tend to produce multiple plants in close proximity - you never see a lone blade of grass, for example. That means a battle for the soil's finite sources, as well as reduction in an individual plant's sunlight exposure due to shadows cast by the others. This is the recipe for Malthusian competition, which underpins the reason behind classical Darwinian natural selection. Growing high and mighty becomes essential to survival, and this directional selection is illustrated in the plant fossil record.

## *How* do trees grow tall?

Biomaterials like wood are not known for their structural homogeneity, and therefore develop imperfections easily. Structurally, this means lower safety factors, and earlier onset of structural instability (for buckling, this is formalised by Perry's analysis, later incorporated into standard engineering design codes based on experiments by Robertson in the 1920s). Trees therefore must respond to structural deviations in their trunk from the vertical. That response is called thigmomorphogenesis, and it is the 'feedback correction' to the more well-known gravitropism (the preference for growth vertically in the first place). Any bending stresses at the roots are amplified by the the fatigue induced by wind loading and thus must be minimised.

An analysis by Greenhill in 1881 showed that an idealised pine tree of uniform trunk diameter 20 inches cannot grow beyond 90 m tall before failing by self-buckling. The actual tallest pine tree is about 83 m tall, which, for its 2 m diameter trunk base, is far below its theoretical limit. While the above Perry-Robertson model of imperfections might go some way to bringing the limit down, another limiting factor in tree height is the transpiration stream that nourishes the leaves, bringing the nutrients in the soil upwards through a constant flow of water. The suction pressure that drives this pump cannot be too strong, or the water high up in the xylem tubes would cavitate, stopping flow and starving the higher leaves.

For most trees, it is in fact this hydrological constraint that limits maximum height, while structural stability guides development up to that limit. To eliminate the bending stresses induced in the base of the trunk due to swaying and leaning, trees have two interesting ways of strengthening themselves: (1) vary the thickness of their trunk cross-section so that they are tapered (thicker at the base, thinner at the top), and (2) reinforce their base on one side only by forming reaction wood to reduce the bending moment about the part of the root. In (McMahon & Kronhauer, 1976), it is shown that the way trees taper their cross-sections (mechanism (1)) is very close to the theoretically optimal distribution of trunk material. What looks like an intelligent design can therefore be explained by the optimising process of natural selection acting on heterotopy.

## Where the common ancestry model comes in

Let's look further at mechanism (2) above, the production of reaction wood in response to asymmetric leaning. Reaction wood is produced by all woody plants, which includes trees. There are two types of reaction wood:

- Compression wood, which is rich in the biopolymer lignin, is produced on the inner side of the leaning trunk (the side in compression), pushing up. Compression wood is the type of reaction wood produced in all gymnosperms (softwoods, non-flowering plants).

- Tension wood, which is rich in the biopolymer cellulose, is produced on the outer side of the leaning trunk (the side in tension), pulling down. Tension wood is the type of reaction wood produced in most angiosperms (hardwoods, flowering plants).

Seems like a clear-cut divide - the two big divisions of trees fit neatly into two different reaction wood types. Sounds like the beauty of design! But wait, what's that sneaky word 'most' doing in that second point? As is all too common in biology, there's always something that wants to be different...

*Amborella* is the only clade that bucks the trend: it's an angiosperm that produces compression wood, like the gymnosperms, instead of tension wood, like its fellow angiosperms. At this point, we demand to know the answer to the following question:

"What is the evolutionary relationship between Amborella, the other angiosperms, and the gymnosperms?"

Evolution predicts nested hierarchies of traits. If the same trait pops up in multiple relatively unrelated groups of organisms, then although one mutation can be invoked to explain the trait in one such group, multiple independent mutations must be invoked to explain all of them. This is far less likely, and therefore has far weaker explanatory power, and is then shunted down the list of scientifically backed possibilities to explain the data at hand. This is where the principle of parsimony (more generally, Occam's razor) is core to modern evolutionary theory. The phylogenetic tree structures recovered from genetic studies must at least somewhat match the trees deduced from more holistic observations, like traditional comparative anatomy. A counterexample to evolution's parsimony is a way to falsify evolution (that's your Precambrian bunny type of thing).

So anyway, what's the answer to the question above?

Molecular phylogenetic studies find that Amborella is the most evolutionarily basal extant angiosperm lineage (i.e. it is the sister clade to all other flowering plants). This divergence pattern is therefore entirely consistent with the predictions of evolutionary theory: the parsimonious conclusion is that the tension wood trait evolved once in the lineage leading to all other angiosperms after their split from Amborella. One new trait, one event in a single lineage - as tidy as it gets.

Think about what it would take to explain this under a separate ancestry hypothesis. We are given that one type of tree is different to the others. Why? Since all separate ancestry models involve an omnipotent deity in the picture, such questions are frequently waved away with "mysterious ways". But that's not science. It's not parsimonious. It has zero explanatory power. As Popper said, a theory that explains everything, explains nothing. If we try to use the bone that modern intelligent design proponents throw us when they claim that form and function are correlated, even this fails here - it's just the evolutionary prediction, but inverted (postdiction: in biology, function (phenotype) follows form (genotype)) and with God slapped on the front because reasons.

~ Branching out

There's also several poetic points about trees worth thinking about that further support evolution's validity:

The 'tree' of life

Evolution's principal model is best illustrated by the tree of life, a highly cross-cultural symbol of origins. The data structure of the binary tree comes up in evolutionary theory because its recursive, ever-branching structure precisely mirrors the recursive, continuous process of speciation (ultimately the reason why cladistics replaced Linnaean taxonomy - there are no privileged ranks other than species, and even species can be ambiguous).

Trees present a counter to irreducible complexity

Trees are climatic climax vegetation, the last and most mature stage of ecological succession, the process by which complex, interconnected, interdependent communities form in newly exposed land. This turns out to be a striking counterexample to the intelligent design (ID) proponents' concept of irreducible complexity (IC): remove one species of an ecosystem and the food webs collapse, and yet we watch ecosystems form in real time. The interdependencies come later; they are not built in from the start. Complex traits in biology evolve in a similar way, with many direct examples known, disproving IC, one of the core pillars of ID.

Trees exemplify the thermodynamic purpose of life

Trees, like all photosynthetic life, are the primary producers for the vast majority of life*: they are responsible for capturing free energy and distributing it out to the rest of their biome's food webs. Sunlight is the sole energy influx into the Earth, a natural free energy gradient that enables the development of non-equilibrium systems that will consume this free energy (high-exergy sunlight) and rapidly generate entropy irreversibly in the environment (water vapour from the transpiration stream output). This is the self-organising principle that makes life compliant and specifically prompted by the laws of physics in the first place, as studied by many from Schrodinger (1944) to Schneider & Kay (1994) to Michaelian (2012, with lots more fascinating research since then) to Hall & McWhirter (2023), with explanatory power in both abiogenesis and evolution.

* exception: chemosynthetic organisms living near deep hydrothermal vents, where sunlight cannot penetrate. Their free energy source is instead the geothermal heat of the Earth, provided via chemical-exergy-rich molecular fuel.

~ Conclusions

So, whether it's the way trees grow structurally or thermodynamically, we see optimisation that could be naively attributed to intelligent design. In a sense, it's not wrong** to say "look at the trees! they show design!" - BUT:

design is incredibly hard to define rigorously and counterexamples spring up as soon as we go beyond what's intuitively known (which happens to be exactly the domain where we look to science for its powerful analytical toolkit, rather than relying on 'common sense' essentially invoked by ID)

nature is more than capable of design! The constraints of biology, and the driving forces of chemistry and physics, work together to create 'goal-oriented design' - selection for functionality, that is. We see the 'goal' because we're intelligent, but we don't invoke literal teleology because we also study the underlying causes. The intuitive appeal of Paley's watchmaker argument - that ID just puts a science-flavoured coat of paint on - funnels one into this fallacious line of reasoning, and is a logical chasm that Dennet separates clearly: from the initial 'design stance', one can either move to the 'intentional stance' or the 'physical stance'. "Why do trees 'want' to grow tall? They must have been programmed to be tall!" No - it's evolutionary dynamics. "Why do tree trunks support themselves so precisely? Programmed!" No - it's feedback system dynamics. "Why do trees 'want' sunlight at all? They must have been programmed to use it!" No - it's thermodynamics! The existence of the designer isn't disproven per se, their alleged actions are just made redundant in the natural world.

** creationists - please, I beg, resist the urge to quotemine me there. Resist temptation, remember the tree in the Garden of Eden... oh hey look we're back to trees again.

Thanks for reading and I hope you enjoyed. As usual I intend to be both educational and persuasive. Oh, and merry Christmas and a happy new year!

## Further citations

- ([Yong, 2025](https://psycnet.apa.org/fulltext/2026-92549-001.html)) - extending the consilience of evolution's body of evidence into the physical sciences, via thermodynamics and information theory.
- [Enrico Coen - *Cells to Civilizations*](https://www.amazon.co.uk/Cells-Civilizations-Principles-Change-Shape/dp/0691165602) (2015) - a book exploring how feedback system dynamics underlies development, the mechanistic basis for evo-devo biology.