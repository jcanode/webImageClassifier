# Resnet Classifier

This is a small web app wrapped a resnet50 image classifier the API is powered by [cortex](https://cortex.dev).

This is my first try into making web apps for machine learning, and dealing with machine learning apis.

The goal was to have this runing on my website [justincanode.com](https://justincanode.com), however, the server I'm using didn't have enough resources to run the website and the necessary docker containers. 

To run this, first install cortex (see the [cortex documentation](https://docs.cortex.dev/install)). Then download the cortex example library, [https://github.com/cortexlabs/cortex](https://github.com/cortexlabs/cortex). Next, from the `examples/tensorflow/image-classifier-resnet50` directory run `cortex deploy` and `cortex get image-classifier-resnet50` to insure that it's running. 

Finally, export the flask app from this directory `export FLASK_APP=main.py` and run `flask run`.

Enter a the url of an image into the form and the next page shows the classes of the image.  
