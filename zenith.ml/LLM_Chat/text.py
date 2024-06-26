transcript = ("Welcome back. So we're working through this introductory series on physics-informed machine learning, "
              "where we're essentially looking at the different opportunities and subtleties of incorporating physics "
              "into the machine learning process. Today we're gonna talk about the second stage of curating the data "
              "or choosing the data that will inform the model. So this is gonna be a little bit of a shotgun of a "
              "lot of different topics because data is so diverse. There are so many aspects of the kinds of data "
              "you're gonna be using to train your models. And so many aspects of the problems you're gonna be trying "
              "to solve and the ways you're gonna solve them, that there's not really just like a one-size-fits-all "
              "thing I can say about how physics is built into the data collection process. So I'm just gonna give "
              "you some kind of ideas that you can use and kind of ruminate on to think about how physics enters into "
              "this data curation process, okay? Now I sometimes joke that this is the, if you're going to build "
              "physics into your machine learning models or learn physics with machine learning, step two is kind of "
              "the Google approach or the Microsoft approach that works really well for big companies that have "
              "nearly infinite amounts of data. If you have enough data of the world, presumably you can learn models "
              "that actually incorporate some of the physics of that world. In principle, biological learning over a "
              "long, long time scale has happened that way. By observing the world, we somehow figured out things "
              "like gravity and F equals MA and real physics through observing the wealth of data that we are "
              "interacting with. But that's a very, very expensive, slow and kind of tedious process. We can't wait "
              "for hundreds of millions of years of evolution with our machine learners. Why don't we as human "
              "experts teach them the things we do know about physics and speed up that process? So a couple of key "
              "things, if we embed physics into our learning process, we can often get away with a lot less data. "
              "This is something I wanna make sure to say upfront because I'm gonna forget to say it later. Let's say "
              "I'm working on a really expensive experiment and it's very difficult to get data samples. Well, "
              "machine learning needs lots of data to train models traditionally. A big neural network needs a lot of "
              "data to train that neural network. If I can incorporate physics to constrain that neural network to "
              "reduce the search space in that neural network, I can often get away with much less data. So for lots "
              "of systems of physical interest and engineering interest, where there's just not that many examples in "
              "the data to draw on, I need physics to allow myself to train those models with less data. So that's an "
              "important point we might come back to later. Good. So we talked about this in the intro video, "
              "this idea that one thing you can do to bake physics into your machine learning model in this data "
              "curation stage, is if there's some data I'm gonna use to generate a machine learning model, "
              "often I know some prior physics, like this system is translation invariant or rotation invariant. And "
              "so what I can do is I can augment my data with copies of the data that I pass through those different "
              "transformations. So for example, if I think that this fluid system that I'm trying to model is "
              "invariant to rotations, like if I rotate things, nothing should change, then in principle, "
              "I can augment my data to include rotated copies and that enriches my data and it stretches out my data "
              "so that less data can go further and train bigger, better models. So that's one way of building in "
              "symmetries and invariants and things like that is just through data augmentation. And we've been doing "
              "this for a long time in classic machine learning and in machine learning for physics and engineering "
              "systems. Okay, good. Another point I wanna make, and this is just absolutely critical, "
              "is the coordinate system in which you measure your data really, really, really, really matters. And "
              "that is an opportunity for your human expertise, for your physical knowledge and intuition to play a "
              "huge role in this machine learning process. So this is one of my favorite videos. It's an illustration "
              "by Mollye and Kristerson of kind of the heliocentric and geocentric views of our solar system. "
              "Geocentrism is where the Earth is at the center of our known universe. The heliocentric model is where "
              "the sun is at the center and everything else orbits around it. And really important point, if I try to "
              "train a machine learning model to predict the motion of all of these colorful dots, if I do it in this "
              "coordinate system, that machine learning model is gonna be working a lot harder. These are much more "
              "complicated curves. They require more terms to explain. The physics is harder to explain in this "
              "coordinate system than this coordinate system. So getting your measurements right and in the right "
              "coordinate system is a huge head start that you can give your machine learning model if you know "
              "something about the right coordinate systems. And again, just like everything I'm telling you in this "
              "physics-informed machine learning, there's kind of a dual or flip side to that, which is sometimes I "
              "don't know the right coordinate system. So I try different coordinate transformations and one of those "
              "machine learning models is gonna train way faster with lower error. That tells me something about, "
              "maybe that's the right coordinate system. So a lot you can do there. And I think about systems where "
              "we don't know the answer, like brain science. So I talked to Bing, Brun, and a lot about this, "
              "about how do you take measurements from the brain and build models of new physics that we haven't "
              "written down for the brain? When we don't even know the first thing about the right coordinate system, "
              "we don't know what's the right transformation of those variables. So discovering those "
              "transformations, discovering the right coordinate systems is an important dual problem. But if you "
              "know something about the physics, if you know that the physics is gonna be simpler in the Fourier "
              "transform domain, Fourier transform your data before you train your model. Good, this can make a huge, "
              "huge difference. And of course, is your data coming from a simulation or an experiment dramatically "
              "changes aspects of your data and how that can be used in a machine learning model. So for example, "
              "oftentimes in simulations, I have a lot more spatial information. I have high resolution spatial "
              "fields that are very hard to get in experiments. It's hard to get an experiment that gives you the "
              "full fluid flow field. But these are pretty expensive. It's hard to run these for a really, really, "
              "really long time. Whereas if I had a wind tunnel experiment, I might not get the full fluid flow "
              "field, but I can run this thing for hours and hours and hours and days and days and days. So "
              "experiments I can often get really long time series of less measurements, less spatial measurements, "
              "maybe just a few points. Simulations I can often get exquisite high resolution detail, but I can't run "
              "them for as long or over as many parameters just because they're expensive to run. Other things to "
              "think about, often experiments have the real nitty gritty details that we don't understand. So usually "
              "these simulations are based on some physics principle, F equals MA, Navier-Stokes equation, "
              "something like that. And if I made an approximation, if there was something I didn't understand about "
              "the physics, it's going to inherently kind of be in this simulation data. So simulation data is "
              "useful, but the gold standard is still building experiments because that's where you're going to see "
              "if your assumptions broke, if your model was wrong. This pendulum here doesn't perfectly match the "
              "Euler-Lagrange equation double pendulum because this one has non-linear friction, non-linear bearing "
              "chatter, non-linear wind resistance, all kinds of little subtle things that are just very hard to put "
              "in that Euler-Lagrange model. So if I had the exact same system simulated, it would be less rich. And "
              "so oftentimes I want my data to be from an experiment, if I can. And a lot of times we're going to be "
              "having these hybrid setups where we have a lot of simulation data, but for a simplified physics. And "
              "we have limited experimental data, but it actually has more realistic physics. So lots of kind of in "
              "between areas where you might have multi-fidelity data sources or data from simulations and "
              "experiments. And I learned this from my colleague, Petros Kumatsakis, who we were writing this review "
              "paper with Baron Noak on machine learning for fluid dynamics. And Petros made the really astute "
              "observation that machine learning in some sense is almost a common data processing framework. It's "
              "like a common set of algorithms for processing data that can help us stitch together data from "
              "simulations and experiments. Different modalities of data, different fidelities, different spatial and "
              "temporal resolutions, we can start stitching those together better with machine learning models. So "
              "all things to be thinking about. What data do you have? And is it enough? Is it rich enough in time, "
              "in space, in parameters? Is it realistic? Are you trying to model something that's already been "
              "modeled? And so you're already baking in those prejudices into your machine learning model? Really "
              "important to think about. And there's some examples where the simulation and the experiment are almost "
              "perfectly matched. This is a cool example of a lab equipment by Quonser, where they have gone through "
              "really painstaking detail, updating their simulation model, their simulated physics, to more closely "
              "match the real experimental system. And sometimes you can actually do that with machine learning. "
              "Sometimes the way you improve your simulation is by learning corrections from your experimental data, "
              "these little machine learning corrections. And oftentimes, in my field of fluid mechanics, "
              "we have really, really big data sets. So if I simulate a fluid flow at full resolution in 3D, "
              "something complicated and turbulent, then a single snapshot of that flow field at one instant in time "
              "might be a gigabyte, or all the way up to petabytes. Some of these simulations are massive, massive, "
              "big data simulations. But you have to ask yourself, is that data useful? Is it rich? Do I have the "
              "time series? Do I know how that data evolves in time? Do I have that flow over different parameters, "
              "different flow velocities, different skin frictions, different things that I actually need to vary in "
              "the real world to design some device or to understand this physics? So sometimes we have really, "
              "really big data, but it's only big in one dimension. It's high spatial resolution, but no parametric "
              "variation, or no time series evolution. Sometimes I have data where I have tons of time series, "
              "but I don't have enough spatial information. So again, this is somewhere where your physical intuition "
              "tells you, huh, is that enough data for me to model something? Is that enough data for me to get "
              "intuition or to use that for design processes? And again, if we're using these models for building "
              "surrogate models that we can then do design optimization on, you would like for your training data to "
              "be somewhat representative of the cases you're going to want to eventually design your system to. So "
              "if I'm trying to optimize a wing for maximizing lift and minimizing drag, I'm going to need training "
              "data that have different shapes and different lifts and different drags. And so if I don't have that "
              "diversity of training data, it's kind of silly to think that I'm going to be able to design this "
              "radically new wing if I just don't have data that varies the geometry and changes the lift and drag. "
              "Even more important, and this is a really important point I want you to think about. I think about "
              "this a lot in shape optimization, aerodynamic optimization, but this really applies to almost all of "
              "these physics problems and engineering problems. A lot of times, we're trying to design a new device "
              "that has never been created before. So maybe I have a cooling fin. I have collaborators in Spain who "
              "are developing these cooling fins. Air flows over these hot fins, and it's supposed to carry the heat "
              "away as fast as possible. Or I work with engineers at automobile companies and aircraft companies, "
              "where you're trying to shape optimization. You're trying to change the shape of a Boeing wing to make "
              "it better performing than any wing you've ever seen before. Well, clearly, that test case, that design "
              "objective, is not in your training data. If it was in your training data, you wouldn't need to be "
              "designing that wing. And if I think about this abstract space of, let's say I have a two dimensional "
              "space where I can vary parameters of this wing, maybe the camber and the aspect or whatever. I can "
              "vary some things about this wing. And each of those points has a different lift and drag a different "
              "performance. I'm trying to find designs that are outside of the distribution I've tested in the past, "
              "because those are going to be new cases that have better performance. What this means, essentially, "
              "is that for design optimization, if I want to design something better than my training data, "
              "then I need my models, my machine learning models, to generalize beyond my training data. Most machine "
              "learning models are excellent at interpolating between the training data that you've already seen. So "
              "if I have five wing geometries that I've built before, it will tell you all of the wing geometries "
              "that are kind of between those. But that's not going to give you a radically new design. For that, "
              "you need your machine learning model to be able to generalize to new shapes and sizes that maybe "
              "haven't been tested before. And this is not a blanket statement, but it's generally true. The way you "
              "get your machine learning model to generalize beyond the training data, maybe for another case that "
              "you haven't seen before, is by baking in physics into those models. Make sure that your models have "
              "the right symmetries and conservation laws, the things you know the physics should have that gives you "
              "a much better chance of them generalizing. Make sure your machine learning models are parsimonious. "
              "They're as simple as possible to describe the data, but no simpler. So use sparsity promoting "
              "regularizing terms in your loss function. We'll talk about that a lot in a couple of lectures. So just "
              "to make this concrete, let's say I'm trying to design a super turbulent baseball or whatever. And I've "
              "only trained on these first three cases. And I've never seen this fourth case, which is the one I "
              "actually want. If I just use naive machine learning, it's only going to be able to interpolate between "
              "these behaviors. And if it's never seen this before, it's never going to be able to predict that. But "
              "if I can bake machine learning physics into my machine learning process, so that my solution satisfy "
              "Navier Stokes, for example, then with that machine learning model, we can run the thought experiment "
              "of increasing the velocity and getting some prediction of what this behavior might be. OK, "
              "that's a big idea, but I really wanted to get that down that often for design, we need to go beyond "
              "our training data. We need physics to generalize those models. OK, other things that are really "
              "important to note is that oftentimes your data is super, super expensive. Think about CERN or LIGO. "
              "These are billions of dollars experiments that give us a few data points. OK, again, this data might "
              "be big in some dimensions, but it's very sparse in other dimensions, very expensive measurements. And "
              "so again, this kind of data is often not big enough to build a deep neural network model, "
              "the kind that we would do for image classification where we have millions of images. This data is much "
              "more expensive, much harder to come by, much more limited. And so again, you have to be more clever "
              "about how you incorporate this data into a machine learning model. Just like physicists, they design "
              "these experiments to be so specific that they can answer a really specific physics question with a "
              "couple of numbers that come out of these experiments. We need to be more clever about how we set up "
              "these machine learning architectures and problems to leverage this very expensive, rare data. Other "
              "things I think about a lot in the data aspect is data bias. So when we think about drug discovery, "
              "material science discovery, there's a lot of bias in our data, because typically our training data is "
              "only examples of things that actually worked. Maybe our training data is a library of actual proteins, "
              "DNA that actually generates real functional proteins. But for every functional protein, there's this "
              "almost infinite space of garbage proteins that don't work at all. And you don't see that in your "
              "training data. So there's this massive data bias. You're often biased towards things that work or work "
              "in the traditional way when you train on this kind of data. So again, something you need to think "
              "about is what biases are in my data. If I'm trying to discover a new material I've never seen before "
              "or a new protein I've never seen before, you need to think really hard about what aspects do you need "
              "your training data to have or your architecture or your problem statement so that you can actually do "
              "that discovery process. So data bias is a big issue. We think about rare events. There's another form "
              "of data bias if you think about it. So I have colleagues like Themisapsis at MIT who think about these "
              "extreme events in dynamical systems. So we all know that there are waves in the ocean. Sometimes "
              "they're fun waves. Sometimes they're catastrophic destructive waves. And we would like to build "
              "machine learning models of how likely these row waves are, how big they can get, maybe predict when "
              "and where they will occur. But the kind of difficulty here is, these are inherently extremely rare "
              "outlier events. So if I have training data of ocean waves, 99.999% of them are not rogue waves. Kind "
              "of by definition, the things that are anomalous that are rare that I actually want to capture because "
              "they're the ones that are going to wipe out an oil rig, those are extremely rare in the data. And so "
              "you have this massive data bias that the vast majority of your data is not the thing you actually want "
              "to be capturing. So if I build a machine learning model, and 99.99% of that data is boring, "
              "and one out of 10,000 records is interesting, I can build an extremely accurate machine learning model "
              "just by focusing on this boring data here and just ignoring the existence of these rare events. "
              "Whereas that's not what you want your machine learning model to do. So there's a lot of work that we "
              "do either to balance the data to kind of like, artificially increase the weight of these rare events "
              "so that they don't just get washed out in the training process. And also, again, incorporating physics "
              "at various stages in the machine learning process. So the dynamics are being captured accurately so "
              "that you can run these models for long enough that you can actually see some of these rare events in "
              "those machine learning models. But rare events and that kind of data bias really important to be aware "
              "of as well. If the thing you want to model is a needle in a haystack, you need to make it look more "
              "like a stack of needles for your machine learning model. And along the same lines of rare events and "
              "expensive experiments are, oftentimes the thing I need to model is a very small, very subtle signal. "
              "So this is a picture I found on Wikipedia that illustrates the transit of Mercury. So if you don't "
              "know the story, Google transit of Mercury. Essentially, you have your classic Newtonian physics which "
              "predicts the motion of the planets and the moons and objects in the solar system pretty accurately. We "
              "have a pretty good understanding of how things actually move in the solar system with just F equals MA "
              "physics. But there is this small discrepancy in the data of how Mercury moves around the sun. A small "
              "discrepancy, Newton's second law doesn't perfectly capture this motion. And so this was actually one "
              "of the big success stories of relativity is in showing that if you add general relativity, essentially "
              "gravitational effects and warping that you can correct F equals MA and much more accurately capture "
              "this motion of Mercury. So really big success story in physics. One of the kind of great modern "
              "success stories is this transit of Mercury being explained by Einstein's relativity. But if you think "
              "about it, if I just measured this data, the effective Newton's second law explains like 99 or 99.9% of "
              "this motion. And Einstein's relativity is only required for capturing that tiny last little bit. So if "
              "I'm training the machine learning model and it's just trying to minimize error or loss, it's almost "
              "certainly gonna pick Newton's second law. It's gonna be very hard to get it to figure out that next "
              "big step because the signal of the thing that makes the difference is so small. We as humans through "
              "our logic and our inductive induction and our scientific method have created entire processes of "
              "science so that we can take very small signals and understand is that small signal real or is it "
              "measurement noise? And if it's real, how do I start to really probe what is the physics that explains "
              "that discrepancy? That's very hard to do in machine learning but that's something that human guidance "
              "really is still important. So you might have a system where there's something really important, "
              "really fundamental you need to model but it's a small signal. It's getting washed out by a much bigger "
              "signal. That's something to keep in mind. And this actually reminds me of one of my favorite stories "
              "in the history of science. This is something I've talked a lot about with my friend Nathan Kutz. We've "
              "written papers on this. So we all know about the famous Galileo ball drop experiment where we drop two "
              "spheres of different density and they fell at the same rate and hit the ground at the same time. But "
              "again, we know that spheres of different density as they reach different velocities will have a lot of "
              "interesting fluid physics that is neglected in this kind of simplistic story. So Galileo was trying to "
              "show that there's a gravitational constant, a constant acceleration. But if you really look closely at "
              "the data, if you really collect really good measurements of this and use wildly different densities of "
              "balls, beach balls and bowling balls, they will follow different rates because there is extra physics "
              "here that's not being modeled by just simple constant gravity f equals ma. There's this extra fluid "
              "physics that isn't captured there. So this is a diagram I think I pulled from NASA which shows the "
              "drag coefficient as a function of velocity is actually very complicated. And that's entirely unmodeled "
              "in this simple ball drop experiment. Presumably Galileo picked two densities that were dense enough "
              "that this could be kind of neglected. And that was a very strategic human guided decision not to drop "
              "a beach ball, but to drop denser objects so that we could kind of ignore this detail in the data. And "
              "really interesting, if you actually drop balls of different densities and you start to see these fluid "
              "effects, you'll actually find that the more classic and incorrect model of Aristotle that these balls, "
              "their kind of motion depends on their inertia or their density, that actually fits the data better. "
              "There's a reason that Aristotle came up with that model. It's because if you throw a wiffle ball "
              "versus a baseball, they really do behave differently because of this extra fluid force. Which, "
              "you know, this is just kind of a cautionary tale that when you're, you know, when you're collecting "
              "data, you need to be thinking, what parts of it do I really want to model? Are there confounding "
              "factors that are not important? You know, those extra complicated physics bits. And maybe you actually "
              "want to model those. Maybe that's an opportunity for modeling with machine learning. But, you know, "
              "humans throughout history have strategically chosen what parts of their data to ignore and what parts "
              "to focus on. And we're just now starting to understand, you know, how that is going to impact the "
              "machine learning era, right? Our machines don't ignore bits of the data unless you help them and guide "
              "them in what to look at. Hidden variables, this is one of the things that is like fundamental in "
              "engineering systems and physical systems. Most of the systems we interact with, we don't have access "
              "to all of the variables that are important for that system. And we have to build models on partial "
              "information, okay? So, you know, think about your playing poker with someone. You don't have all of "
              "the information and you have to make good decisions. If I am, you know, measuring a brain and I'm "
              "trying to prevent seizures or something like that, there's all kinds of hidden states in that brain "
              "that I'm not able to measure or access. If I'm interacting with a fluid system, if I have a wing going "
              "through a fluid, at least as it's flying, I don't have access to measure all of the fluid flow field "
              "around that wing. There's hidden variables in most systems and machine learning actually provides a "
              "really powerful opportunity to start filling in details in those hidden measurements. So as an "
              "example, again, I have like a whole video on this. I'll put a link to it. This is like a whole lecture "
              "topic that we'll get into later. But if I want to model a physical system like this, you know, "
              "Lorentz differential equation, this chaotic Lorentz system, to actually model it as a differential "
              "equation, I would need access to all three states of the system, X, Y and Z. But oftentimes I only "
              "have access to a single measurement, maybe just the X coordinate. So I only see the X coordinate as "
              "this thing's going around. How can I use this partial information and machine learning to start "
              "filling in the gaps, to start filling in this picture just from these partial measurements? It's a "
              "really important problem we think about a lot is what can we do with partial data? You know, "
              "can we recover something that is at least qualitatively similar to my original system from these "
              "partial measurements? So this is, again, something that we rely on dynamical systems theory and "
              "physics to tell us when this is possible and when this isn't possible, okay? That can guide when you "
              "do or don't use machine learning to try to fill in these states. So this is just a tiny teaser. "
              "There'll be a whole, you know, video on this paper, but, you know, we are finding that there actually "
              "are advanced machine learning architectures, deep neural networks that can start to fill in that "
              "missing data and actually give you the full state representation of your system. So this is a teaser "
              "from that paper where, again, you know, in that Lorentz system, we only measure the X coordinate. We "
              "didn't measure Y or Z. But using a custom neural network, you can start to find a coordinate "
              "transformation that describes the full state of the system and you can start learning differential "
              "equations that describe the evolution of that new state. So this is an example of, from a single "
              "measurement, a single scalar measurement of the X coordinate of this Lorentz system, we can start "
              "learning how to embed that through some neural network coordinate transformation in a way that we get "
              "a simple explanatory differential equation out. Now, you don't have to understand how all of this "
              "works. There'll be a whole video on it, but the upshot is lots of times you don't get to measure "
              "everything you want to measure in your system. Most of the time, there are loads of hidden variables, "
              "hidden things that you can't measure, and you still need good models and good predictions. And there's "
              "a lot of opportunities there with machine learning. Okay, last thing, we're gonna talk about digital "
              "twin. Repeatedly, this is one of the big motivations, one of the big industrial engineering "
              "applications of physics-informed machine learning is actually starting to build digital models of "
              "physical assets so we can do improved optimization and design and control. And again, it's always "
              "based on real-world data. So the data you have is gonna be the lifeblood of machine learning models. "
              "It's gonna be the lifeblood of your digital twin. And that's going to increasingly enable better "
              "engineering design and optimization and control and things like that. So, when we think about a "
              "digital twin, I think about having lots of diverse sources of data, kind of a multi-fidelity set of "
              "data sources. Some are cheap and low fidelity, some are very, very expensive and rare, but you need "
              "those for kind of ground truth. Let's say I'm designing an aircraft, I'm gonna run a lot of "
              "low-fidelity simulations to get rough and dirty design improvements. Then I might run some of those "
              "through a high-fidelity simulation. I might run some laboratory tests to calibrate my high-fidelity "
              "models and then eventually I'm actually gonna build the thing and fly it, okay? And it just gets more "
              "expensive every time. That data is gonna be used, that curated data is gonna be used to build our "
              "machine learning models, which we're gonna call our digital twin, that we eventually want to do "
              "optimization over. Now, what I've drawn here is a set of data going into the machine learning model. "
              "So, the machine learning model is, you know, drawing on all of this data that we've collected. But in "
              "the future design optimizations, when I'm designing the next super material, super alloy or super "
              "composite, when I'm designing the next aircraft wing or automobile geometry, I don't just wanna take "
              "all of the data I traditionally collect and feed it into a model. That's very expensive to collect "
              "this data the old fashioned way. What I would love to do is have my machine learning model, "
              "my digital twin have an estimate of how much uncertainty that model has for different configurations, "
              "for different design inputs. So, if I am trying to design wings, then I would like my digital twin, "
              "not just to give me an estimate of the lift and the drag for a particular wing geometry, but to also "
              "tell me how uncertain or certain it is of that estimate. And based on that uncertainty, then we can "
              "actually design a tieback between that digital twin, so that if it has a high uncertainty, "
              "but the design is promising, it can actually go back and collect more data. And it can collect data at "
              "different fidelity based on its uncertainty. So in a way, this is kind of an optimal way of generating "
              "data through active learning, through this kind of feedback between the digital twin machine learning "
              "model and the actual data generation. So this is an advanced concept. Again, we're gonna go into this "
              "in depth in our digital twin module, but it's really important. Sometimes you just have a static data "
              "set, someone emailed you the data, or the person that was working on the project before you collected "
              "the data, and now it's your job to model it, that's fine. But if you're really designing this new "
              "system to do better design optimization for an engineering system, it would be really nice if you "
              "actually had this tieback so you can actually query different fidelity simulations and experiments to "
              "inform that model. It's gonna be way cheaper, way more efficient and faster and performant. Okay, "
              "so this is increasingly going to be how we design really complex systems in the future. And again, "
              "it's gonna give us the best of both worlds, lower cost and lower error. So if these field measurements "
              "have low error but high cost and these low fidelity models have low cost but high error, "
              "can our machine learning model synthesize that into a model that is low cost and low error? And then "
              "we design and optimize over that surrogate model. Okay, good, so that was the big picture mile high of "
              "this second stage of the process, the curating the data. Again, I'm not telling you how to curate your "
              "data. This is a very subtle process. It depends, sometimes you have data and you have to decide on a "
              "problem that you can answer with that data. Sometimes you have a problem and you have to decide what "
              "is the data I could possibly use to solve that problem. Most of the time, you're kind of in this "
              "middle ground where there's types of data you can get, some are cheap, some are expensive, "
              "there's types of problems you wanna solve, some are more ambitious, some are less ambitious. And so "
              "you're gonna spend a lot of time iterating in these two stages here. Okay, coming up soon, "
              "architectures, loss functions and optimizations. This is kind of the glamorous side of machine "
              "learning but it's also really neat. There's a lot of innovation and cool architectures and things you "
              "can do in these next ones. So I'm looking forward to that and I hope you are too. All right, thank you.")
