---

title: "Look at the trees! Evolution and engineering in action"
subtitle: A short essay on trees from an engineering perspective, and its implications for evolution and design
date:
summary:
draft: false
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

Writeup for reddit: [here](https://www.reddit.com/r/DebateEvolution/comments/1pwj75f/but_just_look_at_the_trees_they_show_the_power_of/) (modified for blog format).

## *Why* do trees grow tall?

Plants have embarked on the thermodynamically-Sisyphean task of getting carbon dioxide to *do stuff for them*, rolling carbon-containing molecules up the [Gibbs free energy](https://en.wikipedia.org/wiki/Thermodynamic_free_energy#:~:text=The%20free%20energy%20is%20the%20portion%20of%20any%20first%2Dlaw%20energy%20that%20is%20available%20to%20perform%20thermodynamic%20work%20at%20constant%20temperature%2C%20i.e.%2C%20work%20mediated%20by%20thermal%20energy) mountain (the [Calvin cycle](https://en.wikipedia.org/wiki/Calvin_cycle) of photosynthesis) to make food molecules (glucose and carbohydrates) which release the energy back to them (respiration), before starting over. In human-centric life, we think of CO$_2$ as a [waste product](https://spitfireresearch.com/why-direct-air-capture-dac-sucks-and-not-in-a-good-way/#:~:text=Let%E2%80%99s%20be%20clear%20about%20what%20CO2%20is%3A%20it%E2%80%99s%20a%20waste%20material) that's good for nothing except anthropogenic global warming: it's the end product of both our individual respiration and our species' industrial-scale combustion of fossil fuels, not a starting point.

{{< figure src="gibbs-free-energy-CO2.png" title="Standard Gibbs free energies of formation $ \Delta_f G^{\ominus} $ for some small molecules, showing CO$_2$ at the bottom of an energetic 'pit', and larger molecules like traditional petroleum-derived fuels (representative of plant fuels like glucose) towards the top. Converting CO$_2$ to other chemicals - whether by plants for their food, or by industry for carbon capture and utilisation - therefore requires energy input. Source: Figure 6 of ([Jiang *et al.*, 2010](https://www.researchgate.net/publication/44691024_Turning_carbon_dioxide_into_fuel))." >}}

Plants get away with using CO$_2$ as their *input* because they have *the Sun*, beaming in limitless free energy to a planet that would otherwise be isolated and lifeless. Of course, it wasn't plants who came up with this trick. That goes back to the original photosynthetic microorganisms, a phylum of prokaryotes called [cyanobacteria](https://en.wikipedia.org/wiki/Evolution_of_photosynthesis). Ancient protists, like the ancestors of algae, just took control of this mini-generator and put it into an organelle (endosymbiosis) that we now call the chloroplast.

{{< figure src="calvin-cycle.png" title="The Calvin cycle occurs in the chloroplasts of plants. Biochemical energy in the form of ATP (and the cofactor NAPDH) is produced by the [light-dependent reactions](https://en.wikipedia.org/wiki/Light-dependent_reactions), which is then consumed in the light-independent reactions to fix carbon dioxide into larger organic molecules." >}}

Once multicellular, plant evolution was guided by one rule: 
 
$$ \text{more sunlight → more energy → more growth → more sunlight.} $$
 
Since more growth also comes with more reproduction via further seed dispersal and germination, this positive feedback became subject to natural selection.

The problem is, trees don't grow in a vacuum. When seeds fall to land, they tend to produce multiple plants in close proximity - you never see a lone blade of grass, for example. That means a battle for the soil's finite sources, as well as reduction in an individual plant's sunlight exposure due to shadows cast by the others. This is the recipe for [Malthusian competition](https://en.wikipedia.org/wiki/Modern_synthesis_%2820th_century%29#/media/File:Modern_Synthesis.svg), which underpins the reason behind classical Darwinian natural selection (the '[struggle for existence](https://en.wikipedia.org/wiki/Struggle_for_existence)'). Unless you opt for a [symbiotic strategy](https://en.wikipedia.org/wiki/Biological_interaction#:~:text=Long%2Dterm%20interactions%20(symbioses)%5Bedit%5D), growing taller than your conspecifics becomes essential to survival, and this directional selection is illustrated in the [plant fossil record](https://treescharlotte.org/tree-education/a-brief-history-of-trees/).

## *How* do trees grow tall?

Biomaterials like wood are [not known](http://www.international-agrophysics.org/Influence-of-wood-anisotropy-on-its-mechanical-properties-in-relation-to-the-scale,110808,0,2.html) for their structural homogeneity, and therefore develop imperfections easily. Structurally, this means lower [safety factors](https://en.wikipedia.org/wiki/Factor_of_safety), and earlier onset of structural instability (for buckling, this is formalised by [Perry's analysis](https://en.wikipedia.org/wiki/Perry%E2%80%93Robertson_formula), later incorporated into standard engineering design codes based on experiments by Robertson in the 1920s). Trees therefore must respond to structural deviations in their trunk from the vertical. That response is called [thigmomorphogenesis](https://en.wikipedia.org/wiki/Thigmomorphogenesis), and it is the 'feedback correction' to the more well-known [gravitropism](https://en.wikipedia.org/wiki/Gravitropism) (the preference for growth vertically in the first place). Any bending stresses at the roots are amplified by the the fatigue induced by wind loading and thus must be minimised.

An analysis by [Greenhill in 1881](https://martingillie.wordpress.com/wp-content/uploads/2013/11/longest-column.pdf) showed that an idealised pine tree of uniform trunk diameter 20 inches cannot grow beyond 90 m tall before failing by [self-buckling](https://en.wikipedia.org/wiki/Self-buckling). The actual tallest pine tree is about 83 m tall, which, for its 2 m diameter trunk base, is far below its theoretical limit. While the above Perry-Robertson model of imperfections might go some way to bringing the limit down, another limiting factor in tree height is the [transpiration stream](https://en.wikipedia.org/wiki/Transpiration_stream) that nourishes the leaves, bringing the nutrients in the soil upwards through a constant flow of water. The suction pressure that drives this pump cannot be too strong, or the water high up in the xylem tubes would cavitate, stopping flow and starving the higher leaves of their [craved electrolytes](https://www.youtube.com/watch?v=qqT16kXIQRo).

For most trees, it is in fact this hydrological constraint that limits maximum height, while structural stability guides development up to that limit. To eliminate the bending stresses induced in the base of the trunk due to swaying and leaning, trees have two interesting ways of strengthening themselves: 

1. **vary the thickness of their trunk** cross-section so that they are tapered (thicker at the base, thinner at the top), and
2. **reinforce their base on one side only** by forming [reaction wood](https://en.wikipedia.org/wiki/Reaction_wood) to reduce the bending moment about the part of the root. 

This motif of positive and negative feedback systems interacting to produce optimised structures is a common one in biology. Enrico Coen's book [*Cells to Civilizations* (2015)](https://www.amazon.co.uk/Cells-Civilizations-Principles-Change-Shape/dp/0691165602) gives several concrete examples, with a focus on how feedback system dynamics underpin development, the mechanistic basis for [evo-devo biology](https://en.wikipedia.org/wiki/Evolutionary_developmental_biology). In ([McMahon & Kronhauer, 1976](https://www.sciencedirect.com/science/article/abs/pii/002251937690182X)) and ([Kanahama & Sato, 2023](https://www.nature.com/articles/s41598-023-45468-7)), it is shown that the way trees taper their cross-sections (mechanism (1)) is very close to the theoretically optimal distribution of trunk material. What looks like an intelligent design can therefore be explained by the optimising process of natural selection acting on [heterotopy](https://en.wikipedia.org/wiki/Heterotopy).

{{< figure src="taper-trunk.png" title="Tree trunks have a variable thickness to keep their base stable." >}}

## Where the common ancestry model shines

Let's look further at mechanism **(2)** above, the production of reaction wood in response to asymmetric leaning. Reaction wood is produced by all [woody plants](https://en.wikipedia.org/wiki/Woody_plant), which includes trees. There are two types of reaction wood:

- **Compression wood**, which is rich in the biopolymer lignin, is produced on the inner side of the leaning trunk (the side in compression), pushing up. Compression wood is the type of reaction wood produced in all [**gymnosperms**](https://en.wikipedia.org/wiki/Gymnosperm) (softwoods, non-flowering plants).

- **Tension wood**, which is rich in the biopolymer cellulose, is produced on the outer side of the leaning trunk (the side in tension), pulling down. Tension wood is the type of reaction wood produced in most [**angiosperms**](https://en.wikipedia.org/wiki/Angiosperms) (hardwoods, flowering plants).

{{< figure src="reaction-wood.png" title="Comparison of tension wood (TW) and compression wood (CW). Source: [Osaka University](http://www.nogimasaya.com/favorite/learn-the-wood-structures/)." >}}

Seems like a clear-cut divide - the two big divisions of trees fit neatly into two different reaction wood types. Sounds like the beauty of design! But wait, what's that sneaky word 'most' doing in that second point? As is all too common in biology, there's always something that wants to be different...

[*Amborella*](https://en.wikipedia.org/wiki/Amborella) is the only clade that bucks the trend: it's an angiosperm that produces compression wood, like the gymnosperms, instead of tension wood, like its fellow angiosperms. At this point, we demand to know the answer to the following question:

**"What is the evolutionary relationship between Amborella, the other angiosperms, and the gymnosperms?"**

Evolution predicts nested hierarchies of traits. If the same trait pops up in multiple relatively unrelated groups of organisms, then although one mutation can be invoked to explain the trait in one such group, multiple independent mutations must be invoked to explain all of them. This is far less likely, and therefore has far weaker explanatory power, and is then shunted down the list of scientifically backed possibilities to explain the data at hand. This is where the [principle of parsimony](https://evolution.berkeley.edu/phylogenetic-systematics/reconstructing-trees-cladistics/reconstructing-trees-parsimony/) (more generally, Occam's razor) is core to modern evolutionary theory. The phylogenetic tree structures recovered from genetic studies must at least somewhat match the trees deduced from more holistic observations, like traditional comparative anatomy. A counterexample to evolution's parsimony is a way to falsify evolution (that's your [Precambrian bunny](https://en.wikipedia.org/wiki/Precambrian_rabbit) type of argument from Haldane).

So anyway, what's the answer to the question above?

Molecular phylogenetic studies find that *Amborella* is the **most evolutionarily basal extant angiosperm lineage** (i.e. it is the sister clade to all other flowering plants). This divergence pattern is therefore entirely consistent with the predictions of evolutionary theory: the parsimonious conclusion is that the tension wood trait evolved once in the lineage leading to all other angiosperms after their split from Amborella. One new trait, one event in a single lineage - as tidy as it gets.

{{< figure src="tree_evolution.png" title="The phylogenetic relationship between gymnosperms (non-flowering plants) and angiosperms (flowering plants), showing *Amborella* as the earliest diverging angiosperm. The simplest conclusion is that compression wood is the ancestral trait, while tension wood appeared only once after *Amborella* split from the other angiosperms. Image source: Figure 1 of ([Williams, 2012](https://www.researchgate.net/publication/233834460_Pollen_Tube_Growth_Rates_and_the_Diversification_of_Flowering_Plant_Reproductive_Cycles))." >}}

Think about what it would take to explain this under a separate ancestry hypothesis. We are given that one type of tree is different to the others. Why? Since all separate ancestry models involve an omnipotent deity in the picture, such questions are frequently waved away with "mysterious ways". But that's not science. It's not parsimonious. It has zero explanatory power. As Popper said, a theory that explains everything, explains nothing. If we try to use the bone that modern intelligent design proponents throw us when they claim that [form and function are correlated](https://en.wikipedia.org/wiki/Form_follows_function), even this fails here - it's just the evolutionary prediction, but inverted ([postdiction](https://en.wikipedia.org/wiki/Postdiction): in biology, function (phenotype) follows form (genotype)) and with God slapped on the front because reasons.

## Branching out

There's also several poetic points about trees worth thinking about that further support evolution's validity:

**The 'tree' of life**

Evolution's principal model is best illustrated by the [tree of life](https://www.evogeneao.com/en/explore/tree-of-life-explorer), a highly [cross-cultural symbol of origins](https://en.wikipedia.org/wiki/Tree_of_life). The data structure of the [binary tree](https://en.wikipedia.org/wiki/Binary_tree) comes up in evolutionary theory because its recursive, ever-branching structure precisely mirrors the recursive, continuous process of speciation (ultimately the reason why cladistics replaced Linnaean taxonomy - there are no privileged ranks other than species, and even species can be ambiguous and is semi-arbitrary with its many [species concepts](https://researchdata.museum.vic.gov.au/forum/wilkins_species_table.pdf)).

{{< figure src="tree-diagram.png" title="**Left:** Darwin's original concept of diversification as the way new species originate, showing a tree structure. **Right:** The modern concept of a phylogenetic tree, capable of representing all relationships between life, past and present, with only minor exceptions due to well-understood mecahnisms (e.g. horizontal gene transfer, incomplete lineage sorting)." >}}

**Trees present a counter to irreducible complexity**

Trees are [climatic climax vegetation](https://en.wikipedia.org/wiki/Climax_community), the last and most mature stage of [ecological succession](https://en.wikipedia.org/wiki/Ecological_succession), the process by which complex, interconnected, interdependent communities form in newly exposed land. This turns out to be a striking counterexample to the intelligent design (ID) proponents' concept of irreducible complexity (IC): remove one species of an ecosystem and the food webs collapse, and yet we watch ecosystems form in real time. The interdependencies come later; they are not built in from the start. Complex traits in biology evolve in a similar way, with many direct examples known, disproving IC, one of the core pillars of ID.

{{< figure src="ecological-succession.png" title="Trees indicate mature ecosystems, only appearing once pioneers and smaller plants have appeared. Once trees are established, the mutualistic interdependencies like mycorrhizal fungi and tree roots are locked in. Source: [University of Chicago](https://news.uchicago.edu/explainer/what-is-ecological-succession)." >}}

**Trees exemplify the thermodynamic purpose of life**

Trees, like all photosynthetic life, are the primary producers for the vast majority of life*: they are responsible for capturing free energy and distributing it out to the rest of their biome's food webs. Sunlight is the sole energy influx into the Earth, a natural free energy gradient that enables the development of [non-equilibrium systems](https://en.wikipedia.org/wiki/Non-equilibrium_thermodynamics) that will consume this free energy (high-exergy sunlight) and rapidly generate entropy irreversibly in the environment (water vapour from the transpiration stream output). This is the self-organising dissipative structuring principle that makes life compliant and specifically prompted by the laws of physics in the first place, as studied by many from [Schrödinger](https://en.wikipedia.org/wiki/What_Is_Life%3F) (1944) to [Schneider & Kay](https://www.sciencedirect.com/science/article/pii/0895717794901880) (1994) to [Michaelian](https://www.thriftbooks.com/w/thermodynamic-dissipation-theory-of-the-origin-and-evolution-of-life-salient-characteristics-of-rna-dna-and-other-fundamental-molecules-suggest-an-origin-of-life-driven-by-uv-c-light_karo-michaelian/23415119/#edition=15276109&idiq=25515015) (2010s) to contemporary interdisciplinary discourse as reviewed in ([Hall & McWhirter, 2023](https://royalsocietypublishing.org/doi/10.1098/rsta.2022.0290)) and ([Yong, 2025](https://psycnet.apa.org/fulltext/2026-92549-001.html)), with explanatory power in both abiogenesis and evolution.

{{< figure src="thermo-life.png" title="A hierarchical view of the closed Earth system in which thermodynamics constrains the processes that generate free energy from low-entropy sunlight (yellow boxes) that then fuels the dissipative dynamics of Earth system processes. Source: [Kleidon, 2023](https://earthsystem.org/2023/09/19/new-paper-working-at-the-limit-how-entropy-work-and-limits-shape-earth-system-functioning-here-is-a-simple-but-long-summary-of-the-key-points/)." >}}

\* *exception: [chemosynthetic](https://en.wikipedia.org/wiki/Chemosynthesis) organisms living near deep hydrothermal vents, where sunlight cannot penetrate. Their free energy source is instead the geothermal heat of the Earth, provided via [chemical-exergy](https://en.wikipedia.org/wiki/Exergy#Chemical_exergy)-rich molecular fuel.*

## Conclusions

So, whether it's the way trees grow structurally or energetically, we see optimisation that could be naively attributed to intelligent design. In a sense, it's not wrong to say *"look at the trees! they show design!"* - BUT:

- **Design is incredibly hard to define rigorously**, and counterexamples spring up as soon as we go beyond what's intuitively known (which happens to be exactly the domain where we look to science for its powerful analytical toolkit, rather than relying on '[common sense](https://loveofallwisdom.com/blog/2010/11/science-is-not-common-sense/)' essentially invoked by ID)

- **Nature is more than capable of design!** The constraints of biology, and the driving forces of chemistry and physics, work together to create 'goal-oriented design' - selection for functionality, that is. We see the 'goal' because we're intelligent, but we don't invoke literal [teleology](https://en.wikipedia.org/wiki/Teleology_in_biology) because we also study the underlying causes. The intuitive appeal of Paley's watchmaker argument - that ID just puts a science-flavoured coat of paint on - funnels one into this fallacious line of reasoning, and is a logical chasm that [Dennet separates clearly](https://en.wikipedia.org/wiki/Intentional_stance#Dennett's_three_levels): from the initial 'design stance', one can either move to the 'intentional stance' or the 'physical stance'. "Why do trees 'want' to grow tall? They must have been programmed to be tall!" **No** - it's evolutionary dynamics. "Why do tree trunks support themselves so precisely? Obviously programmed." **No** - it's feedback system dynamics. "Why do trees 'want' sunlight at all? Programmed!" **No** - it's thermodynamics! The existence of the designer isn't disproven *per se*, their alleged actions are just made redundant in the [natural world](https://en.wikipedia.org/wiki/Naturalism_(philosophy)#Methodological_naturalism).

It could be argued that the role of the deity is not to create life directly, but to set up the laws of physics and initial conditions that make life inevitable. In my opinion, ths universe-scale fine tuning argument, valid or not, leads more towards theistic or deistic evolution rather than overt creationism or intelligent design - as evidenced by its support by most scientifically literate theists since the mid-20th century (e.g. Lemaître, founder of Big Bang cosmology) - and is therefore not contrary to the validity of evolution as a theory. The success of evolutionary algorithms in modern computer software demonstrates that when the *rules of the game* are intelligently designed, evolution follows naturally, with no further external intervention required as the world's trajectory unfolds. If there *is* something behind it all, it must be unfathomably powerful.

Thanks for reading and I hope you enjoyed. As usual I intend to be both educational and persuasive. Oh, and merry Christmas and a happy new year!