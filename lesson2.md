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
