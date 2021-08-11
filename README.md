# smart-teaching-using-human-FER-model
FER- facial emotion Recognition(FER) model

Keep ready of the following files in a folder in your system

1. testthis.py
2. basic_backend_code.py
3.server.py
4.activate_this.py
5. team dominators final.ipynb
6. project notebook.ipynb

save these models too 
1. fer.h5
2. fer.json
3. EmotionDetectionModel.h5
4.haarcascade_frontalface_default
5.fer_backup.h5
6. fer_backup.json


dataset : FER2013 dataset. (" upload this to google drive") 


install the anaconda navigator from this site "[https://repo.anaconda.com/archive/Anaconda3-2021.05-Windows-x86_64.exe](url)"

go to google colab platform "[https://colab.research.google.com/notebooks/intro.ipynb?utm_source=scs-index](url)"
>file>upload motebok> upload the file no 5. "team dominators.ipynb" >open it >   Run time >   change Run time type> select GPU> then come out of that> Run all

mount the drive  ( same account shld be used in which the dataset is been upoaded ), when asked in the second line of code with the authorisation code/link which will be displayed while running

once the training of epoches is done, run furthur 4-5 lines of code


open anaconda prompt shell(if installed)
type the following commands one by one wait for them to install fully (WHEN ASKED PRESS YES DURING INSTALLATION)

1. conda create -n majorproenv python=3.6
2. conda activate majorproenv
3. conda install tensorflow
4. conda install keras
5. conda install pandas
6. conda install opencv
7. conda install nb_conda
8. conda install flask 


(majorproenv) C:\Users\dell>jupyter notebook

**IMP*
project is implemented in linux platform

save all the necessary files in a separate folder which are easily accessible 
open terminal window and open your virtual environment (if not created ,  refrer to this "[https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/26/python-virtual-env/](url)"

download the datasset from this link [https://www.kaggle.com/deadskull7/fer2013](url)

go to your virtual environment in the terminal(linux)/command prompt(windows), and type "testthis.py" this will open a new window , prompt permission to switch on
camera if asked and you can see the emotions getting detected,similarly run "basic_backend_code.py".

install "IP webcam" app from your mobile(android)
connect both you mobile and laptop/desktop to a single data connection network/wifi.

then open server.py file in editor window(pycharm/any IDE tools),type theexact url which is displayed on the "IP webcam"app when the camera is on then type the ame url in the  "server.py" file (for ref: t starts with https://.....)

once its done, come back to terminal window, run/execute the "server.py" file.and there you go its done. you must see a web application window where you must look into your mobile not the laptop/desktop and observe the change of emotions in the laptop/desktop screen.

Thank you.





  



