package com.callor.hello;

import java.util.Random;

public class Var_06 {

	public static void main(String[] args) {
		Random rnd = new Random();
		
		int num1 = rnd.nextInt(100) + 1;
		if (num1 % 3 == 0) {
			int num2 = +num1;
			
			System.out.println(num2 + "3의 배수들의 합");
		}

	}

}
