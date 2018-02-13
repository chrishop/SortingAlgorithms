
import java.util.Random;

public class BubbleSort{

	public static void main(String[] args){
	
		int[] list1 = generateUnsortedList();
		printList(list1);
		System.out.println(list1.length);
		list1 = bubbleSort(list1);
		System.out.println();
		printList(list1);


	}
	
	/*
	 * creates an 100 long list in which the numbers range from 0 to 1000
	 */
		
	public static int[] generateUnsortedList(){
	
		
		Random rand = new Random();
		int[] intarr = new int[100];


		for (int i=0 ; i<intarr.length ; i++){
	
			intarr[i] = rand.nextInt(1001);

		}

		return intarr;
	
	}

	/*
	 * prints the list in a formatted fashion 
	 * 5 numbers on each row
	 */

	public static void printList(int[] theList){
		int counter = 0;
		for(int i = 0; i<theList.length ; i++){
		
			System.out.print(theList[i]);
			System.out.print(",");

			if (counter < 5){
		
				counter++;
			
			}else{
			
				counter = 0;
				System.out.print("\n");	
			
			}
		}
		System.out.println("");
	}

	/*
	 * uses your basic bubble sort to sort the numbers
	 */

	public static int[] bubbleSort(int[] theList){
		
		int temp;

		for (int i = 0 ; i<(theList.length) ; i++){
			for(int j = 0 ; j<theList.length-1 ; j++){
			
				if (theList[j] > theList[j+1]){
				
					temp = theList[j];
					theList[j] = theList[j+1];
					theList[j+1] = temp;
				}
			}
		}
		return theList;
	}
}
