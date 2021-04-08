# Plushkin's Helper

This is a simple console tool which can help you to clean your folders 
removing duplicates.  
Required features:
- find duplicate files in a folder;
- remove duplicate allowing the user to choose which file should be kept.

## Usage

`usage: plushkin.py [-h] [--delete] path`

### Usage as a simple console tool  

Output:  
`python3 plushkin.py /path/to/dir`  

Interactive removing of duplicates:  
`python3 plushkin.py --delete /path/to/dir`

### Usage via Docker  

Build docker image:  
`docker build --tag plushkin .`  

There are 2 ways to run the script:  
1. via shell
```
sudo docker run -ti -v {/path/to/dir}:/app/data plushkin /bin/bash  
python plushkin.py /data  
python plushkin.py --delete data/  
```
2. via <i>docker run</i> args
```
docker run -ti -v {/path/to/dir}:/app/data plushkin python3 plushkin.py data/  
docker run -ti -v {/path/to/dir}:/app/data plushkin python3 plushkin.py --delete data/  
```  
  
#### Example output
```
$ python3 plushkin.py files/  
Size: 810 bytes  
[1]: /home/dmitriy/Desktop/test_task_oi/files/file1.txt (Created: 08-04-2021)  
[2]: /home/dmitriy/Desktop/test_task_oi/files/file4.txt (Created: 08-04-2021)  
[3]: /home/dmitriy/Desktop/test_task_oi/files/file5.txt (Created: 08-04-2021)  
[4]: /home/dmitriy/Desktop/test_task_oi/files/file6.txt (Created: 08-04-2021)  
[5]: /home/dmitriy/Desktop/test_task_oi/files/file404.txt (Created: 08-04-2021)  
[6]: /home/dmitriy/Desktop/test_task_oi/files/file3.txt (Created: 08-04-2021)  
----------------------------------------------------------------------  
Size: 5.1 MB  
[1]: /home/dmitriy/Desktop/test_task_oi/files/song3.mp3 (Created: 08-04-2021)  
[2]: /home/dmitriy/Desktop/test_task_oi/files/song2.mp3 (Created: 08-04-2021)  
[3]: /home/dmitriy/Desktop/test_task_oi/files/dir1/song4.mp3 (Created: 08-04-2021)  
[4]: /home/dmitriy/Desktop/test_task_oi/files/dir2/dir3/song5.mp3 (Created: 08-04-2021)  
----------------------------------------------------------------------  
Size: 2.04 MB  
[1]: /home/dmitriy/Desktop/test_task_oi/files/rec4.m4a (Created: 08-04-2021)  
[2]: /home/dmitriy/Desktop/test_task_oi/files/rec2.m4a (Created: 08-04-2021)  
[3]: /home/dmitriy/Desktop/test_task_oi/files/rec3.m4a (Created: 08-04-2021)  
[4]: /home/dmitriy/Desktop/test_task_oi/files/rec1.m4a (Created: 08-04-2021)  
----------------------------------------------------------------------  
```

#### Example of interactive removing of duplicates
```
$ python3 plushkin.py --delete files
Size: 810 bytes
[1]: /home/dmitriy/Desktop/test_task_oi/files/file1.txt (Created: 08-04-2021)
[2]: /home/dmitriy/Desktop/test_task_oi/files/file4.txt (Created: 08-04-2021)
[3]: /home/dmitriy/Desktop/test_task_oi/files/file5.txt (Created: 08-04-2021)
[4]: /home/dmitriy/Desktop/test_task_oi/files/file6.txt (Created: 08-04-2021)
[5]: /home/dmitriy/Desktop/test_task_oi/files/file404.txt (Created: 08-04-2021)
[6]: /home/dmitriy/Desktop/test_task_oi/files/file3.txt (Created: 08-04-2021)
----------------------------------------------------------------------
Choose file to keep by entering its number or press enter to skip it
1
File /home/dmitriy/Desktop/test_task_oi/files/file1.txt was kept

Size: 5.1 MB
[1]: /home/dmitriy/Desktop/test_task_oi/files/song3.mp3 (Created: 08-04-2021)
[2]: /home/dmitriy/Desktop/test_task_oi/files/song2.mp3 (Created: 08-04-2021)
[3]: /home/dmitriy/Desktop/test_task_oi/files/dir1/song4.mp3 (Created: 08-04-2021)
[4]: /home/dmitriy/Desktop/test_task_oi/files/dir2/dir3/song5.mp3 (Created: 08-04-2021)
----------------------------------------------------------------------
Choose file to keep by entering its number or press enter to skip it
3
File /home/dmitriy/Desktop/test_task_oi/files/dir1/song4.mp3 was kept

Size: 2.04 MB
[1]: /home/dmitriy/Desktop/test_task_oi/files/rec4.m4a (Created: 08-04-2021)
[2]: /home/dmitriy/Desktop/test_task_oi/files/rec2.m4a (Created: 08-04-2021)
[3]: /home/dmitriy/Desktop/test_task_oi/files/rec3.m4a (Created: 08-04-2021)
[4]: /home/dmitriy/Desktop/test_task_oi/files/rec1.m4a (Created: 08-04-2021)
----------------------------------------------------------------------
Choose file to keep by entering its number or press enter to skip it
4
File /home/dmitriy/Desktop/test_task_oi/files/rec1.m4a was kept
```