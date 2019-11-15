#!/bin/bash

# For the existed directories a object_labels file will be created with all the
# objects' labels in the videos in this directory.

image_folder="images/"

# Save files in this directory
folder="files"
mkdir $folder
# save files
file_listdir=$folder/"listdir"
file_objs=$folder/"object_labels"
# groundtruth files
file_groundtruth="groundtruth_labels"
file_path="obj_paths"

#echo $file_path
cat $file_path|while IFS=, read -r col1
do
  if [ ! -d "${image_folder}${col1:: -9}" ]; then
    echo "${image_folder}${col1:: -9}"
  else
    echo "$col1" |& tee -a $file_listdir
  fi
done < $file_path


cat $file_listdir|while IFS=, read -r col1
do
  cat $file_groundtruth|while IFS=, read -r col2
  do
         
    if [[ $col2 == $col1* ]]; then
      prefix="${col2%$col1}" # remove sufix
      sufix=${col2#"$col1"} # remove prefix
      echo "$sufix" |& tee -a $file_objs
    fi
  done < $file_groundtruth
done < $file_listdir
