load trainData.txt
load trainTags.txt
load testData.txt
load testTags.txt
svmStruct = svmtrain(trainData,trainTags);
output = svmclassify(svmStruct,testData);
dlmwrite('svm-output.txt',output);
accuracy =sum(output==testTags)/length(testTags);
s = horzcat('svm_accuracy = ',num2str(accuracy*100),'%');
disp(s);

