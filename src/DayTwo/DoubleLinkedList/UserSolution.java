package DayTwo.DoubleLinkedList;
class Node {
    public int data;
    public Node prev;
    public Node next;

    public Node(int data) {
        this.data = data;
        this.prev = null;
        this.next = null;
    }
    public Node(){
        this.prev=null;
        this.next=null;
    }
}

public class UserSolution {

    private final static int MAX_NODE = 10000;

    private Node[] node = new Node[MAX_NODE];
    private int nodeCnt = 0;
    private Node head;

    public Node getNode(int data) {
        node[nodeCnt] = new Node(data);
        return node[nodeCnt++];
    }

    public void init() {
        head=new Node();
    }

    public void addNode2Head(int data) {
        Node new_node=getNode(data);
        if(head.next==null){
            head.next=new_node;
            new_node.prev=head;
        }
        else{
            new_node.next=head.next;
            new_node.prev=head;
            head.next.prev=new_node;
            head.next=new_node;
        }
    }

    public void addNode2Tail(int data) {
        Node new_node=getNode(data);
        Node tmp=head;
        while(tmp.next!=null){
            tmp=tmp.next;
        }
        new_node.prev=tmp;
        tmp.next=new_node;
    }

    public void addNode2Num(int data, int num) {
        int index=1;
        if(num==1){
            addNode2Head(data);
        }
        else{
            Node new_node=getNode(data);
            Node tmp=head;
            while(tmp!=null){
                if(index==num){
                    break;
                }
                tmp=tmp.next;
                index+=1;
            }
            if(tmp.next!=null) {
                new_node.next=tmp.next;
                new_node.prev=tmp;
                tmp.next.prev=new_node;
                tmp.next=new_node;
            }
            else{
                new_node.prev=tmp;
                tmp.next=new_node;
            }
        }
    }

    public int findNode(int data) {
        Node tmp=head;
        int index=0;
        while(tmp.data!=data){
            tmp=tmp.next;
            index+=1;
            if(tmp.next==null){
                break;
            }
        }
        return index;
    }

    public void removeNode(int data) {
        //없어도 삭제가 됨.
        int flag=0;
        Node tmp=head;
        Node tmp2=head.next;
        while(tmp2.data!=data){
            tmp=tmp.next;
            tmp2=tmp2.next;
            if(tmp2.next==null){
                flag=1;
                break;
            }
        }
        if(tmp2.next!=null){
            tmp.next=tmp2.next;
            tmp2.next.prev=tmp;
        }
        else{
            if(flag==0){
                tmp.next=null;
            }
        }
    }

    public int getList(int[] output) {
        Node tmp=head;
        int index=0;
        while(tmp.next!=null){
            tmp=tmp.next;
            output[index]=tmp.data;
            index+=1;
        }
        return index;
    }

    public int getReversedList(int[] output) {
        Node tmp=head;
        Node tmp2=head;
        int index=0;
        while(tmp.next!=null){
            tmp=tmp.next;
        }
        while(tmp.prev!=head){
            output[index]=tmp.data;
            tmp=tmp.prev;
            index+=1;
        }
        output[index]=tmp.data;
        index+=1;
        return index;
    }
}