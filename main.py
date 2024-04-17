import os
import pandas as pd
import numpy as np
import shutil



def newest_journal(path):
    files = os.listdir(path)
    paths = [os.path.join(path, basename) for basename in files]
    paths = filter(lambda x: x.endswith('.docx'), os.listdir('.'))
    # print (paths)
    # print (max(paths, key=os.path.getctime))
    return max(paths, key=os.path.getctime,default=0)
def newest_video(path):
    files = os.listdir(path)
    paths = [os.path.join(path, basename) for basename in files]
    paths = filter(lambda x: x.endswith('Pro.mp4'), os.listdir('.'))
    # print (paths)
    # print (max(paths, key=os.path.getctime))
    return max(paths, key=os.path.getctime,default=0)


# onedrivepath="C:/Users/batuhansayis/OneDrive - University of Cambridge/JOURNALING STUDY DATASET"
# onedrivepath="C:/Users/batuhansayis/Desktop/JOURNALINGSTUDYDATASET"

onedrivepath = "E:/WINDOWS_BACKUP_16042024/Onedrive/JOURNALING_STUDY_DATASET"


enter_directory_path = "C:/Users/batuhansayis/Desktop/"
input_folder_name = "JEPMEN TRIALS FINAL/"
output_folder_name = "JEPMENPIPELINEPROJECT/"
output_directory_path = enter_directory_path + output_folder_name
input_directory_path = enter_directory_path + input_folder_name
input_directory_path2 = onedrivepath
main_loop_start_count = 0
# main_loop_end = 42
main_loop_end = 1

video_splitter_path = 'C:/Users/batuhansayis/Desktop/video-splitter-master'
journal_output_directory = 'C:' + '\\' +  'Users' + '\\' + 'batuhansayis' + '\\' +  'Desktop' + '\\' + 'JEPMEN_JOURNAL_VIDEO_DATASET'


#
# order = pd.read_csv(order_file)
maindataframe = pd.DataFrame()
test = []


for x in os.listdir(input_directory_path2):
    if os.path.isfile(x):
        print('f-', x)
    elif os.path.isdir(x):
        print('d-', x)
    elif os.path.islink(x):
        print('l-', x)
    else:
        test.append(str(x))


def create_outputfolder(folder_name):
    os.chdir(folder_name)
    for i in range(main_loop_start_count, main_loop_end):

        os.mkdir(test[i])
        os.chdir('./' + test[i])

        os.mkdir('Session2')
        os.mkdir('Session4')
        os.mkdir('Session1')
        os.mkdir('Session3')

        os.chdir('..')

def create_outputfoldertree(journal_output_directory):
    if not os.path.exists(journal_output_directory):
        os.mkdir(journal_output_directory)
        create_outputfolder(journal_output_directory)
    else:
        shutil.rmtree(journal_output_directory)
        os.mkdir(journal_output_directory)
        create_outputfolder(journal_output_directory)

create_outputfoldertree (journal_output_directory)
os.chdir(input_directory_path2)


def movemp4(source_path,destination_path):
    list = []
    for x in os.listdir(source_path):
        if os.path.isfile(x):
            list.append(str(x))
    list_mp4 = []
    for i in range(0, len(list)):
        if list[i].endswith(".mp4"):
            # list_mp4.append(list[i])
            shutil.move(list[i], destination_path)

def cut_video(videofile_name,destination_path):
    return_path = os.getcwd()
    manifest_path = return_path + '\manifest.csv'
    video_path = return_path + '\\' + videofile_name


    os.chdir(video_splitter_path)

    os.system("python ffmpeg-split.py -f " + video_path + " -m " + manifest_path)
    source_path = os.getcwd()
    print (source_path)
    print(destination_path)
    movemp4(source_path,destination_path)


    os.chdir(return_path)
    print (videofile_name)


def isjournalsession():
    os.chdir('./' + '0005-Journaling')
    print(os.getcwd())
    journal_name = newest_journal('.')

    if journal_name == 0:
        print('no journal')
        result = 0
    else:
        print (journal_name)
        result = 1
    os.chdir('..')
    return result
def find_session(no_session,participant_no):
    name = os.getcwd()
    destination_path= journal_output_directory + '\\' +participant_no +'\\'+no_session

    listdirectory= ([name for name in os.listdir(".") if os.path.isdir(name)])

    matching = [s for s in listdirectory if no_session in s]

    if len(matching) == 1:
        result = matching[0]
        os.chdir('./' + result )

        is_journal = isjournalsession()
        if is_journal == 1:
            os.chdir('./' + '0004-Camera')
            print(os.getcwd())
            videofile_name = newest_video('.')
            if videofile_name == 0:
                print ('no video')
            else:
                cut_video(videofile_name,destination_path)
            os.chdir('..')
            os.chdir('..')
        else:
            os.chdir('..')
            os.chdir('..')
    else:
        print('no folder')


for i in range(main_loop_start_count, main_loop_end):
    print(os.getcwd())
    os.chdir('./' + test[i])

    find_session('Session2',test[i])
    find_session('Session4',test[i])
    find_session('Session1',test[i])
    find_session('Session3',test[i])

    os.chdir('..')

os.chdir(output_directory_path)
