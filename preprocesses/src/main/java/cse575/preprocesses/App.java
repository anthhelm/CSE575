package cse575.preprocesses;
import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.HashMap;
import java.util.Map;

public class App {

	public static void main(String [] args) throws IOException{
		String line;
		Integer i=1,j=1;
	    Map<String,Integer> productids= new HashMap<String,Integer>();
	    Map<String,Integer> userids= new HashMap<String,Integer>();
		try {
			
			/*Specify the output file path of the python script preprocess.py below */
			
			BufferedReader csvfileinput = new BufferedReader(new FileReader(new File("/home/nikhil/cse575/CSE575/preprocessinter.csv")));
			csvfileinput.readLine();
			 while((line=csvfileinput.readLine()) != null){
				    //System.out.println(line);
					String [] eachvalue=line.split(",");
					if(productids.get(eachvalue[0]) == null)
					{
					    productids.put(eachvalue[0],i++);
					}
					
					if(userids.get(eachvalue[1]) == null)
					{
						userids.put(eachvalue[1],j++);
						System.out.println(j);
					}
			 }
	        FileWriter csvfileoutput =new FileWriter(new File("/home/nikhil/cse575/CSE575/preprocessfinal.csv"));     
	        csvfileoutput.append("UserID,ProductID,Review");
	        csvfileoutput.append("\n");
	        
	    BufferedReader csvfileinputfinal = new BufferedReader(new FileReader(new File("/home/nikhil/cse575/CSE575/preprocessinter.csv")));
	    csvfileinputfinal.readLine();
	    while((line=csvfileinputfinal.readLine()) != null){
				String [] eachvalue=line.split(",");
				productids.get(eachvalue[0]);
				userids.get(eachvalue[1]);
				csvfileoutput.append(userids.get(eachvalue[1]) +","+productids.get(eachvalue[0])+ ","+eachvalue[2]);
				csvfileoutput.append("\n");
		 }
	        csvfileinput.close();
	        csvfileinputfinal.close();
	        csvfileoutput.close();		 
		} catch (FileNotFoundException e) {
				e.printStackTrace();
		}	
	}
	
}
