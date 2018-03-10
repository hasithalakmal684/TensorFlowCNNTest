import random;
from mnist import MNIST;

def loadMNISTData(dataset = "training",path = "samples", mndata = MNIST("")):
    
    if dataset is "training":
        return mndata.load_training();
    elif dataset is "testing":
        return mndata.load_training();
    else:
        raise (ValueError, "dataset must be 'testing' or 'training'");

def mnistDataRandomTest(dataset,path):
    mndata = MNIST(path);

    images,labels = loadMNISTData(dataset,path,mndata);
    
    index = random.randrange(0,len(images));
    print(mndata.display(images[index]));
    

def main():
    
    path = "samples";
    dataset= "training"; #or testing
    
    mnistDataRandomTest(dataset,path);

if __name__=="__main__":
    main();