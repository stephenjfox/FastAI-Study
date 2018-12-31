 [오후 8시 51분]

 Found a number of cool competitions on Kaggle that cover the basic machine
   learning tasks that need to be done:
* [Humpback Whale Identification](https://www.kaggle.com/c/humpback-whale-identification)
* [Google Store Revenue Prediction](https://www.kaggle.com/c/ga-customer-revenue-prediction)
* [Merchant Category Recommendation](https://www.kaggle.com/c/elo-merchant-category-recommendation)
* [Human Protein Altas Image Classification](https://www.kaggle.com/c/human-protein-atlas-image-classification)
  + This is for smart microscopy used in medical diagnostics, among __many__ other
	  tasks

[ImageNet Object __Localization__ Competition](https://www.kaggle.com/c/imagenet-object-localization-challenge)

I started digging into the Whales competition, and the library is showing
  some of its cracks.
* Maybe the functionality is improved in the v1 release, but there's a bug in the
  batch size coming through as `1` and throws a `ValueError`

[A bulleted list of notes](https://forums.fast.ai/t/wiki-lesson-3/9401/33) points
  to [a great explanation of deep network memory requirements](https://www.graphcore.ai/posts/why-is-so-much-memory-needed-for-deep-neural-networks)
* And effectively clarifies the shortcomings of some architectures

[Fast.AI Rachel's introduction to Tabular data](https://www.fast.ai/2018/04/29/categorical-embeddings/)

---

__I've finished lesson 3__. Given the aforementioned struggles, I'm going to
  dig into the problems with my usage of the library and figure out why it's so
  hard to whale watch!
