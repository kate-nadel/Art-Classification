# Art-Classification

![img](https://raw.githubusercontent.com/perceptionmgmt/Art-Classification/main/img.pdf)

Final project for Machine Learning (INFO 656) course at Pratt Institute with Amir Imani


### Project description
Build a neural network that can classify works of art from the Museum of Modern Art’s collection by their medium. Ultimately my project is to create a neural network to classify whether a work of art is a lithograph or not a lithograph. Once I have this completed I can expand from a binary classification to a multi-class classification neural net.


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
For this binary classification, save an equal amount of lithographs as non lithographs
```
for idx, row in tqdm(df[df['Target'] == False].head(50).iterrows(), total=df.shape[0]):
    save_images(row['ThumbnailURL'], row['ObjectID'], "../data/images/")

for idx, row in tqdm(df[df['Target'] == True].head(50).iterrows(), total=df.shape[0]):
    save_images(row['ThumbnailURL'], row['ObjectID'], "../data/images/")
```

2. Refine the dataframe so that it includes a “foreign key” which connects the ObjectID (also how the images are titled) to whether or not it is a lithograph (the target, or y)


3. Load and resize the images

4. Connect the target to the actual training images (create the classes/labels)

5. Build the model

6. Fit the model

7. Test it & expand data



### Findings & Discussion
