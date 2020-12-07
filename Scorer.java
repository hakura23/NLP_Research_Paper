import java.io.*;
import java.util.*;

public class Scorer{
	public static void main(String[] args){
		List<String> output = new ArrayList<>();
		List<String> key = new ArrayList<>();
		List<String> words = new ArrayList<>();
		List<Integer> lines = new ArrayList<>();
		HashMap<String, Integer> hm = new HashMap<>();
		hm.put("LOC_PER", 0);
		hm.put("ORG_PER", 0);
		hm.put("O_PER", 0);
		hm.put("PER_LOC", 0);
		hm.put("ORG_LOC", 0);
		hm.put("O_LOC", 0);
		hm.put("PER_ORG", 0);
		hm.put("LOC_ORG", 0);
		hm.put("O_ORG", 0);
		hm.put("PER_O", 0);
		hm.put("ORG_O", 0);
		hm.put("LOC_O", 0);

		try{
			BufferedReader reader = new BufferedReader(new FileReader(args[0]));
	        String line = reader.readLine();
	        int count = 1;
	        while (line != null){
	        	if(line.length() != 0){
	        		String[] curr = line.split("\t");
	        		words.add(curr[0]);
	        		lines.add(count);
	        		output.add(curr[1]);
	        	}
	            line = reader.readLine();
	            count++;
	        }
	        reader.close();
		}
		catch(IOException ex){
        	System.out.println(ex.getMessage());
		}
		try{
			BufferedReader reader = new BufferedReader(new FileReader(args[1]));
	        String line = reader.readLine();
	        while (line != null){
	        	if(line.length() != 0){
	        		String[] curr = line.split("\t");
	        		key.add(curr[1]);
	        	}
	            line = reader.readLine();
	        }
	        reader.close();
		}
		catch(IOException ex){
        	System.out.println(ex.getMessage());
		}

		System.out.println(output.size() + " " + key.size());
		double correct = 0;
		double outputSize = 0;
		double keySize = 0;
		try{
			File file = new File(args[0] + "_mismatch.txt");
      		file.createNewFile();
      		FileWriter myWriter = new FileWriter(args[0] + "_mismatch.txt");

      		for(int i = 0; i < output.size(); i++){
				if(!output.get(i).equals("O")){
					if(key.get(i).equals("O")){
						String temp = output.get(i) + "_O";
						hm.put(temp, hm.get(temp) + 1);
					}
					outputSize++;
				}
				if(!key.get(i).equals("O")){
					keySize++;
				}
				if(!key.get(i).equals("O")){
					if(output.get(i).equals(key.get(i))){
						correct++;
					}
					else{
						if(output.get(i).equals("LOC")){
							String temp = "LOC_" + key.get(i);
							hm.put(temp, hm.get(temp) + 1);
						} 
						else if(output.get(i).equals("PER")){
							String temp = "PER_" + key.get(i);
							hm.put(temp, hm.get(temp) + 1);
						}
						else if(output.get(i).equals("ORG")){
							String temp = "ORG_" + key.get(i);
							hm.put(temp, hm.get(temp) + 1);
						}
						else if(output.get(i).equals("O")){
							String temp = "O_" + key.get(i);
							hm.put(temp, hm.get(temp) + 1);
						}
						myWriter.write(lines.get(i) + "\t" + words.get(i) + "\t" + output.get(i) + "\t" + key.get(i) + "\n");
						//PER: LOC, PER: 
					}
				}
			}
			myWriter.close();
		}
		catch(IOException ex){
        	System.out.println(ex.getMessage());
		}
		

		

		double precision = correct/outputSize;
		double recall = correct/keySize;
		double fMeasure = 2/((1/precision) + (1/recall));

		System.out.println("Precision: " + precision + "\n" +
							"Recall: " + recall + "\n" + 
							"F-Measure: " + fMeasure);
		double totalError = 0;
		for(String str: hm.keySet()){			
			totalError += (double)hm.get(str);
		}
		System.out.println("\nOutput_AnswerKey: ErrorCount" + "\t" + "ErrorPercent");
		for(String str: hm.keySet()){			
			double percent = ((double)hm.get(str))/totalError;
			System.out.println(str + ": " + hm.get(str) + "\t" + percent);
		}
	}
}