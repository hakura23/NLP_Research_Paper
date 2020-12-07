import java.io.*;

public class Remover{
	public static void main(String[] args){
		try{
			BufferedReader reader = new BufferedReader(new FileReader(args[0]));
	        String line = reader.readLine();
    		File file = new File(args[0] + "TestFormatted.txt");
      		file.createNewFile();
      		FileWriter myWriter = new FileWriter(args[0] + "TestFormatted.txt");
	        while (line != null){
	        	if(!line.equals("\t")){
	        		String[] curr = line.split("\t");
	        		myWriter.write(curr[0] + "\n");
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
