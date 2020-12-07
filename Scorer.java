import java.io.*;
import java.util.*;

public class Scorer{
	public static void main(String[] args){
		List<String> output = new ArrayList<>();
		List<String> key = new ArrayList<>();
		try{
			BufferedReader reader = new BufferedReader(new FileReader(args[0]));
	        String line = reader.readLine();
	        while (line != null){
	        	if(line.length() != 0){
	        		String[] curr = line.split("\t");
	        		output.add(curr[1]);
	        	}
	            line = reader.readLine();
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

		for(int i = 0; i < output.size(); i++){
			if(!output.get(i).equals("O")){
				outputSize++;
			}
			if(!key.get(i).equals("O")){
				keySize++;
			}
			if(!key.get(i).equals("O") && output.get(i).equals(key.get(i))){
				correct++;
			}
		}

		double precision = correct/outputSize;
		double recall = correct/keySize;
		double fMeasure = 2/((1/precision) + (1/recall));

		System.out.println("Precision: " + precision + "\n" +
							"Recall: " + recall + "\n" + 
							"F-Measure: " + fMeasure);
	}
}