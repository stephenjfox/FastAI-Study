[2018년 12월 12일]

[오후 9시 8분]

I'm having a terrible time with Paperspace, disappointingly.
* Google Colab was kind of working, but barely (slow to use, different key bindings,
  start from scratch every time)
* Google Cloud has given me some struggles with sub-projects and I don't know how
  to resolve it.
	- Problem: Newly created project (that have less controls) can't make VMs that
	  use GPUs
		* Therefore, I can't use it for the course
* Paperspace has been giving me a world of trouble:
  - Buggy interface to my terminal
	- Non-responsive
	- Can't change my password on my instance?!

I know that I'm going to fast and loose, not pushing through to make anything
  happen.
* I want it to work
  + I'm willing to put in the work to make it work

I'm going to try Paperspace __one more time__, then I'm going to just make the
 instance on my _main account_ in GCP
- Not good security practices.
+ Going to get deliverable

---

May have found my solution...

* It's going in [lesson 1](./lesson1.md), where it belongs

---

[2018년 12월 13일]

[오후 3시 8분]

[Wiki for lesson 2 recap](https://forums.fast.ai/t/wiki-lesson-2/9399)
+ Not a lot of homework
+ Includes links to the next lesson
- Not sure how it connects with the notebook labeled as [`lesson 2`](https://github.com/fastai/fastai/tree/master/courses/dl1)
  - Or why that's different from the [_courses_ project](https://github.com/fastai/courses/tree/master/deeplearning1/nbs)


[2018년 12월 14일]

[오전 11시 51분]

Reading more *__carefully__*, the [Deep Learning for Coders Wiki Root](https://forums.fast.ai/t/part-1-faq/10330) clarifies that:
* The [courses repo](https://github.com/fastai/courses/tree/master/deeplearning1) has __older__ resources
  + Instead, you should be looking in the `courses` folder of the `fastai` project.
  * As I progress through the course, I'll have to vet the legitimacy of this claim
* PyTorch is what you should use to model research-driven experimentation
  + Don't hold back on the infrastructure technologies, if you have 'em
  + But _aim_ then _shoot_
    * Being a Research Scientist is different from a Research Engineer which is different from a Engineer


---

[오전 11시 45분]

In order to maximize my learning and not waste time with (potentially unnecessary)
  data setup, machine configuration, and more, I'm going to write down __what__
  I know, then compare with what Jeremy teaches in these lessons.
* It's taken me a little too long to get through the first and second video
  - I'm relearning, not learning for the first time, so I don't need as much
    explanation as some
  + But I'm not fluent as I used to be: not thinking, talking, and explaining
    regularly has caused a bit of a "drive-up" of my vocabulary and knowledge
* Thankfully, lots of things are being reactivated, which I will now hope to
  articulate


Convolutional Neural Networks
* I don't remember *exactly* where the name comes from, but I recall that the
  mathematical clustering of function application (as CNNs do with kernels) is
  relevant
* Are best done as *very* __deep__ models, hundreds of modules that are 12 dozens
  of layers each, of hundreds of nodes (for things like Inception-V4)
  * [NOTE]: read the Inception-V4/Inception-ResNet paper from 2016
* Manifest the idea of weight-sharing and clusters of nodes (typically in square shapes [e.g. 4x4 pixels all going to one chunk of neurons])
  + Why? Because the a group of neurons activating for the same thing is more
    powerful and efficient than a single neuron firing/activating
  + These groups are responsible for identifying one aspect of the image
    * Lines
      * Edges
      * Curves
    * Gradients
      * Color
      * Hue
    - These aspects are not programmed manually, but with more "layers"/modules
      two things happen:
      + __Modules closer__ to the image-as-raw-pixels acquire more basic things,
        some of which seem so basic that humans can have a hard time articulating
        the distinction between on set of activations and another
      + __Modules further__ away (and thus closer to the output) learn reasoning
        about higher and higher level abstractions
        * What is initially just "shape detection" turns into "tabby vs maine coon"
* Depth also helps fulfill the universal approximation theorem:
  + Each module of depth can improve "power" (efficiency and/or abstraction capacity)
    *exponentially*
    * some variable `x` raised to the input size `n`
  - Broadening, or widening, your layers can only improve power polynomially
    * some input size `n` raised to a variable `x`
* Performing image Classification
  * by utilizing the `softmax` function (which produces a probability distribution
    for some `m` number of classes), rather than an `argmax` (which produces a
    one-hot vector for the same `m` number of classes), we can observe what the
    network _thinks_ a given image ought to be.
  + [NOTE]: Residual Networks (ResNets) have done excellently in recent years
    on this task. Why? What makes them different?
* Performing Object Detection:
  - I don't know much here according to what the field is doing, but I have some
    ideas to how it is done:
  + If you are able to isolate which neurons fire in a specific kernel, for a
    subset of the image-pixels input, you would be able to say "that section is
    a \_\_\_\_"
  + How generally, if a dumb AI had to answer the question "is there a bird in
    this picture", it would just return `if bird detection pixels EVER fired`
  + I've only read one paper on fast object detection, and only recently has my
    interest in it been piqued.

---

TODO: Lookup "Jupyter notebook extensions" or something like it
* Jeremy Howard has collapsible `H1`-tags in my markdown notes, as does Google Colab.
* I would really like that kind of usability in my notebook


[오후 12시 54분]

[Jupy Ext Medium]: https://towardsdatascience.com/jupyter-notebook-extensions-517fa69d2231

Found [a blog post][Jupy Ext Medium] that explains what Jupyter Notebook
  extension are, and a shortlist of those that would be most helpful


[오후 1시 1분]

Jeremy took time to point out that 80% accuracy on a dataset with only two classes
  is __very__ different than an 80% accuracy on a dataset with __120__ classes

[오후 1시 4분]

@1:33:32 - Jeremy points out that the FastAI library lets you scale up training
* If you trained on a smaller image, you can scale up and train on a larger image
  to get further improvements
  - 10k is a small sample size when it comes to deep learning
* Switching to bigger images is a nearly obvious way to avoid overfitting.
  + Fully Convolutional architectures, which VGG-net is __not__, enjoy this property

When your validation loss is lower than your training set score, that means you're
  underfitting
* With `cycle_mult=2`, the epoch go in a sequence of 1 -> 2 -> 4 per learning-rate
  range
* Training further on the [Kaggle Dog breeds competition](www.kaggle.com/c/dog-breed-identification)
  didn't prove fruitful because that dataset was so similar to ImageNet (the source architecture)
  that new weights weren't any different.
  - Turns out it was actually a subset of ImageNet

- A 2017-recent paper deduced that, if you have an unbalanced dataset, you should
  basically throw in copies of the rare cases

---
[오후 1시 16분]

It seems that the students at USF aren't fully satisfied with the hand-waving and
  "we'll explore that" later, because Jeremy has plans to teach those things later
  on in the course, but all the papers and material is shared (in brief) when
  the students ask
* De-Convolution is covered in Part 2, and glanced at in the lesson 7 of Part 1

We'll be talking a lot about architectures
* ResNet34 (trained on ImageNet) is a great starting and ending point
* ResNext50 is stronger, but takes 2-8x longer to train
  + The model was so much stronger that it was overfitting with `cycle_mult=2`
  + Using ResNext50 (which was a hilariously short amount of code) it got 99.75%
    accuracy.
    - Basically __one__ mistake in 1000. That is state-of-the-art
  * Also, this context for that notebook makes me appreciate the lack of text in
    it 지금



---

[12월 16일]

[오후 6시 4분]

[403 error]: https://github.com/Kaggle/kaggle-api/issues/87
[Kaggle rules for dog-breed]: https://www.kaggle.com/c/dog-breed-identification/rules


I was [struggling with a 403][403 error] in pulling the
  dog-bread-Classification dataset from Kaggle.
* Turns out I just needed to [accept the rules][Kaggle rules for dog-breed]

Going to spend a second to get the data on my GCP instance, then I'll code along
  with Jeremy

[오후 6시 14분]

It was really painless.

1. `pip install kaggle` (after `conda activate fastai`)
2. `kaggle competitions download -c dog-breed-identification`
3. Unzip the data as desired: `/data/dogbreed/*.zip` for instance

[오후 7시 4분]

I'm taking longer to work through the video/notebook-template than I wanted, but
  I'm still going through it.
* Part of it is the notebook's unfriendliness to what __I__ am trying to do


---

It ended up being easier to follow along with Jeremy, then introduce my own
  abstractions (there weren't many necessary) as they arose.
* It was less noise and made the learning stick, rather than filling ia a
  prescribed mold.
  + It makes the knowledge *mine* rather than borrowed (and forgotten) from
    someone else
