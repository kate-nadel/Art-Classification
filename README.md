# Art-Classification

![](https://raw.githubusercontent.com/perceptionmgmt/Art-Classification/main/git-images/img.jpeg)

Final project for Machine Learning (INFO 656) course at Pratt Institute with Amir Imani


### Project description
The goal of this project was to build a neural network that can classify works of art from the Museum of Modern Art’s collection by their medium. Ultimately my project is to create a neural network to classify whether a work of art is a lithograph or not a lithograph. Once I have this completed I can expand from a binary classification to a multi-class classification neural net in the future.


### Concept
How do machines “see” art, and what can this tell us about how humans see (and thus classify) art? What kinds of artwork does the neural net misclassify? Why, and what does this say about the work of art itself?


### Data
Data for this project is available from the Museum of Modern Art's [github](https://github.com/MuseumofModernArt/collection). I used the Artworks.csv file.


### Method

1. Started by downloading images from the MoMA dataset
```
def save_images(image_url, image_name, image_dir):
    """
    This function saves an image from image_url to a local path at image_dir/image_name
    """
    file_name = "{}.jpg".format(image_name)
    file_path = os.path.join(image_dir, file_name)

    f = open(file_path,'wb')
    f.write(requests.get(image_url).content)
    f.close()
```
For this binary classification, save an equal amount of lithographs as non lithographs using the data_loader notebook.
I manually organized the images into train & validation folders. With 1800 "TRUE" and 1800 "FALSE" in the train, and 200 of each in the validation folder.

When it comes time to test an image, download one at a time using this data loader into a test folder.


2.  Build a dataframe which includes relevant information. This will be referred to later when testing the model. Create a column with the Target: if the Medium is lithograph, the target is True.

```
lith_condition = df['Medium'].str.lower().str.contains('lithograph')
df['Target'] = lith_condition

df = df[['ObjectID', 'ThumbnailURL', 'Target']]
df.head()
```


3. Load and resize the images using flow_from_directory

```
train_dataset = train.flow_from_directory("../data/images/all/train/",
                                          target_size = (64,64),
                                          batch_size = 25,
                                          class_mode = "binary",
                                         )
```

4. Build the model

This model includes a Conv2D layer, 2 MaxPooling layers, and a flatten layer

5. Fit the model

The model is compiled using the "adam" optimizer, loss is at to "binary_crossentropy," and metrics are set to "accuracy"

I tested the steps_per_epoch and number of epochs, and the results that worked best with the highest accuracy was steps_per_epoch = 12 and epochs = 10

6. Test it!
The accuracy of this model came out to 85.71%

7. I tested one image at a time and then checked the original dataframe's Target column to verify. It worked for that image!
![](https://raw.githubusercontent.com/perceptionmgmt/Art-Classification/main/git-images/Screen%20Shot%202020-12-09%20at%206.34.06%20PM.jpg)

![](https://github.com/perceptionmgmt/Art-Classification/blob/main/git-images/Screen%20Shot%202020-12-09%20at%206.34.18%20PM.jpg)

### Findings & Discussion
