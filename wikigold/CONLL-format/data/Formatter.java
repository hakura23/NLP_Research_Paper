import java.io.*;

public class Formatter{
	public static void main(String[] args){
		try{
			BufferedReader reader = new BufferedReader(new FileReader(args[0]));
	        String line = reader.readLine();
    		File file = new File(args[0] + "AnsFormatted.txt");
      		file.createNewFile();
      		FileWriter myWriter = new FileWriter(args[0] + "AnsFormatted.txt");
	        while (line != null){
	        	if(line.length() != 0){
	        		String[] curr = line.split(" ");
	        		if(curr[1].equals("O")){
	        			myWriter.write(curr[0] + "\tO" + "\n");
	        		}
	        		else{
	        			if(curr[1].split("-")[1].equals("PER")){
	        				myWriter.write(curr[0] + "\tPER" + "\n");
	        			}
	        			else if(curr[1].split("-")[1].equals("ORG")){
	        				myWriter.write(curr[0] + "\tORG" + "\n");
	        			}
	        			else if(curr[1].split("-")[1].equals("LOC")){
	        				myWriter.write(curr[0] + "\tLOC" + "\n");
	        			}
	        			else{
	        				myWriter.write(curr[0] + "\tO" + "\n");
	        			}
	        		}	
	        	}
	        	else{
	        		myWriter.write("\n");
	        	}
	            line = reader.readLine();
	        }
	        reader.close();
	        myWriter.close();
		}
		catch(IOException ex){
        	System.out.println(ex.getMessage());
		}
	}
}