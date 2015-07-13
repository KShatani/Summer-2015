%% deletes first feature ARFF file and saves it as newFileName.ARFF
clear all;

tic
javaaddpath('F:\Weka-3-6\weka.jar');
folderPath = 'D:\KenyaShatani\Data\avec2015\allFeatures\';
newFolderPath = 'D:\KenyaShatani\Data\avec2015\allFeatures\new';
new = 'new';
listOfFiles = dir(folderPath);
totalnFiles = length(listOfFiles);

n = length(listOfFiles)-2; %number of files

fileName = cell(1,n);
for i = 1:1
    
    fileName{1,i} = listOfFiles(i+2).name;
    filePath = strcat(folderPath, fileName(i)); 
    wekaOBJ = loadARFF(filePath);
    
    [mdata,featureNames,targetNDX,stringVals,relationName] = weka2matlab(wekaOBJ,{});
    data = mdata(:, 2:end);
    newfeatureNames = featureNames(2:end);
    name = strcat('newData', i);
    
    newWekaOBJ = matlab2weka(name, newfeatureNames, data,1);
    
    newFilePath = strcat(newFolderPath,new,fileName(i));
    saveARFF(newFilePath,newWekaOBJ);
    
end
toc