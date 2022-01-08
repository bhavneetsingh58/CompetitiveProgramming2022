package com.bhavneetsingh;

public class LinkedListCustom {
    //creating node class
    Node head;
    private int size;

    LinkedListCustom(){
        this.size = 0;
    }

    class Node {
        String data;
        Node next;

        Node(String data){
            this.data = data;
            this.next = null;
            size++;
        }
    }
    //add-first
    public  void AddFirst(String data){
        Node newNode = new Node(data);
        if(head == null){
            head = newNode;
            return;
        }
        newNode.next = head;
        head = newNode;
    }
    //addLast
    public void AddLast(String data){
        Node newNode = new Node(data);
        if(head == null){
            head = newNode;
            return;
        }
        Node currNode = head;
        while (currNode.next != null){
            currNode = currNode.next;
        }
        currNode.next = newNode;
    }
    //printLast
    public void PrintList(){
        if(head == null){
            System.out.println("list is empty");
            return;
        }

        Node currNode = head;
        while (currNode != null){
            System.out.print(currNode.data+"->");
            currNode = currNode.next;
        }
        System.out.println("NULL");
    }
    //DeleteFirst
    public void DeleteFirst(){
        if(head == null){
            System.out.println("list is empty");
            return;
        }
        size--;
        head = head.next;

    }
    //DeleteLast
    public void DeleteLast(){
        if(head == null){
            System.out.println("list is empty");
            return;
        }
        size--;
        if(head.next == null){
            head = null;
            return;
        }

        Node secondLastNode = head;
        Node lastNode = head.next;
        while(lastNode.next != null) {
            lastNode = lastNode.next;
            secondLastNode = secondLastNode.next;
        }
        secondLastNode.next = null;
    }

    public int GetSize(){
        return size;
    }

    public void ReverseList(){
        if(head == null){
            System.out.println("List is empty");
            return;
        }
        if(head.next == null){
            return;
        }
        Node prevNode = null;
        Node currentNode = head;
        Node next = null;
        while(currentNode.next != null){
            next = currentNode.next;
            currentNode.next = prevNode;
            prevNode   = currentNode;
            currentNode = next;
            head = prevNode;

        }

    }


    public static void main(String[] args) {
        LinkedListCustom list = new LinkedListCustom();
        list.AddFirst("this");
//        list.PrintList();
        list.AddLast("is");
        list.AddLast("a");
        list.AddLast("last");
//        list.PrintList();
//        list.DeleteFirst();
//        list.PrintList();
//        list.DeleteLast();
//        list.PrintList();
//        System.out.println(list.GetSize());
//        list.AddFirst("this");
//        list.PrintList();
//        System.out.println(list.GetSize());
        list.ReverseList();
        list.PrintList();

    }

}
