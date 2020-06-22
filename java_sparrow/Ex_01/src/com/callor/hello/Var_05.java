package com.callor.hello;

import java.util.Random;

public class Var_05 {

	public static void main(String[] args) {

		int num1 = 0;
		int num2 = 0;
		Random rnd = new Random();

		num1 = rnd.nextInt(100) + 1;
		num2 = rnd.nextInt(100) + 1;

		if (num1 % 2 == 0) {

			System.out.println(num1 + "는 짝수 입니다.");
		}
		if (num2 % 2 == 0) {

			System.out.println(num2 + "는 짝수 입니다.");
		}
	}

}
