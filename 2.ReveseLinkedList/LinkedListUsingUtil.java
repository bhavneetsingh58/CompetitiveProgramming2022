package com.bhavneetsingh;

import java.util.LinkedList;

public class LinkedListUsingUtil {
    public static void main(String[] args) {
        LinkedList<String> myList = new LinkedList<String>();
        myList.add("is");
        myList.addFirst("this");
        myList.addLast("a");
        myList.add(3,"list");
        for(int i = 0 ; i<= myList.size()-1;i++ ){
            System.out.println(myList.get(i));
        }
        myList.removeFirst();
        myList.removeLast();
        myList.remove(0);
        myList.remove("a");
        System.out.println(myList.contains("is"));
        System.out.println(myList);

    }
}
