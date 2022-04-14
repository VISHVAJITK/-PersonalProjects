#  Face Genration with GAn (General Advesial Nwetwork)
It is a beginer project to understand the GAN, in this project a simple GAN model is trained to generate faces.

## A schematic GAN implementation
The given [notebook]() explain how to implement a GAN in Keras in its barest form.
The specific implementation is  using the  deep
convolutional GAN (DCGAN): a very basic GAN where the generator and discriminator
are deep convnets.

The GAN is trained on images from the Large-scale CelebFaces Attributes dataset
(known as CelebA), a dataset of 200,000 faces of celebrities (http://mmlab.ie.cuhk.edu.hk/projects/CelebA.html) To speed up training, the images are resized to 64 × 64,
so the  generate  images of human faces are 64 × 64.
 Schematically, the GAN looks like this:
- A generator network maps vectors of shape (latent_dim,) to images of shape
(64, 64, 3).
- A discriminator network maps images of shape (64, 64, 3) to a binary score
estimating the probability that the image is real.
- A gan network chains the generator and the discriminator together: gan(x) =
discriminator(generator(x)). Thus, this gan network maps latent space vectors to the discriminator’s assessment of the realism of these latent vectors as
decoded by the generator.-  We train the discriminator using examples of real and fake images along with
“real”/“fake” labels, just as we train any regular image-classification model.
- To train the generator, we use the gradients of the generator’s weights with
regard to the loss of the gan model. This means that at every step, we move the
weights of the generator in a direction that makes the discriminator more likely
to classify as “real” the images decoded by the generator. In other words, we
train the generator to fool the discriminator.

## The Generated Output
![img](https://github.com/VISHVAJITK/mldl_Notes/blob/main/srceen%20shot/gan.png?raw=true)