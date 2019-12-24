// Calculating the coefficients for the reccursive function that verifies if a complex number is in the Mandelbrot set

import java.io.IOException;
import java.util.ArrayList;
import java.util.Scanner;

public class Julia{
	public static void main(String[] args){
		// get input from the user
		//System.out.println("Filler so that it compiles properly");
		int n = Integer.parseInt(args[0]);
		calculate(n);
	}	

	// a method that takes an array of integer coefficients and returns the next array of coefficients
	public static long[] next(long[] arr){
		long[] newArr = new long[arr.length*2-1];
		// calculate the new values
		// for the case where i=0, it's always just gonna be 0, when i=1 it'll be 
		newArr[1]=1;
		for (int i=0;i<arr.length;i++){
			for (int j=0;j<arr.length;j++){
				newArr[i+j] = newArr[i+j]+arr[i]*arr[j];
			}
		}
		return newArr;
	}

	// a method that calculates the arrays for the coeffs for the first n expantions and prints them
	public static void calculate(int n){
		long[] arr = new long[]{0,1};
		for (int i=0;i<n;i++){
			arr = next(arr);
			for (int j=0;j<arr.length;j++){
				System.out.print(arr[j]);
				System.out.print(", ");
			}
			System.out.println("\n");
		}

	}
}


