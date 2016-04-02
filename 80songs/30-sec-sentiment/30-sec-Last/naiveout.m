load trainData.txt
load trainTags.txt
load testData.txt
load testTags.txt
model = fitNaiveBayes(trainData,trainTags);
output = model.predict(testData);
dlmwrite('naive-output.txt',output);
accuracy = (sum(output==testTags)/length(testTags))*100;
s = horzcat('naive_accuracy = ',num2str(accuracy),'%');
disp(s);
