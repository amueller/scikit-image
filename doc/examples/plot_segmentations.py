"""
====================================================
Comparison of segmentation and superpixel algorithms
====================================================

This example compares three popular low-level image segmentation methods.  As
it is difficult do obtain good segmentations, and the definition of "good"
often depends on the application, these methods are usually used for optaining
an oversegmentation, also known as superpixels. These superpixels then serve as
the level of operation for more sophisticated algorithms such as CRFs.


Felzenszwalb's efficient graph based segmentation
-------------------------------------------------
This fast 2d image segmentation algorithm, proposed in [1]_ is popular in the
computer vision community.
The algorithm has a single ``scale`` parameter that influences the segment
size. The actual size and number of segments can vary greatly, depending on
local contrast.

.. [1] Efficient graph-based image segmentation, Felzenszwalb, P.F. and
       Huttenlocher, D.P.  International Journal of Computer Vision, 2004


Quickshift image segmentation
-----------------------------

Quickshift is a relatively recent 2d image segmentation algorithm, based on an
approximation of kernelized mean-shift. Therefore it belongs to the family
of local mode-seeking algorithms and is applied to the color+coordinate space,
see [2]_.

One of the benefits of quickshift is that it actually computes a
hierarchical segmentation on multiple scales simultaneously.

Quickshift has two parameters, one controlling the scale of the local
density approximation, the other selecting a level in the hierarchical
segmentation that is produced.

.. [2] Quick shift and kernel methods for mode seeking,
       Vedaldi, A. and Soatto, S.
       European Conference on Computer Vision, 2008


SLIC - K-Means based image segmentation
---------------------------------------
This algorithm simply performs K-kmeans in the 5d color-coordinate space and is
therefore closely related to quickshift. As the clustering method is simpler,
it is very efficient. It is essential for this algorithm to work in Lab color
space to obtain good results.  The algorithm quickly gained momentum and is now
widely used. See [3] for details.

.. [3] Radhakrishna Achanta, Appu Shaji, Kevin Smith, Aurelien Lucchi,
    Pascal Fua, and Sabine Suesstrunk, SLIC Superpixels Compared to
    State-of-the-art Superpixel Methods, TPAMI, May 2012.
"""
print __doc__

import matplotlib.pyplot as plt
import numpy as np

from skimage.data import lena
from skimage.segmentation import felzenszwalb_segmentation, \
    visualize_boundaries, slic, quickshift
from skimage.util import img_as_float

img = img_as_float(lena()[::2, ::2])
segments_fz = felzenszwalb_segmentation(img, scale=100, sigma=0.5, min_size=50)
segments_slic = slic(img, ratio=10, n_segments=250, sigma=1)
segments_quick = quickshift(img, kernel_size=3, max_dist=6, ratio=0.5)

print("Felzenszwalb's number of segments: %d" % len(np.unique(segments_fz)))
print("Slic number of segments: %d" % len(np.unique(segments_slic)))
print("Quickshift number of segments: %d" % len(np.unique(segments_quick)))

fig, ax = plt.subplots(1, 3)

ax[0].imshow(visualize_boundaries(img, segments_fz))
ax[1].imshow(visualize_boundaries(img, segments_slic))
ax[2].imshow(visualize_boundaries(img, segments_quick))
for a in ax:
    a.set_xticks(())
    a.set_yticks(())
plt.show()