package DayTwo.SingleLinkedList;

class Node {
    public int data;
    public Node next;

    public Node(int data) {
        this.data = data;
        this.next = null;
    }
    public Node(){
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
        new_node.next=head.next;
        head.next=new_node;
    }

    public void addNode2Tail(int data) {
        Node new_node=getNode(data);
        Node tmp=head;
        while(tmp.next!=null){
            tmp=tmp.next;
        }
        tmp.next=new_node;
    }

    public void addNode2Num(int data, int num) {
        int index=1;
        Node tmp1=head;
        Node new_node=getNode(data);
        while(tmp1!=null){
            if(index==num){
                break;
            }
            tmp1=tmp1.next;
            index+=1;
        }
        new_node.next=tmp1.next;
        tmp1.next=new_node;
    }
    public void removeNode(int data) {
        Node tmp=head;
        Node tmp2=head.next;
        while(tmp2.data!=data){
            tmp=tmp.next;
            tmp2=tmp2.next;
            if(tmp2.next==null){
                break;
            }
        }
        tmp.next = tmp2.next;
    }

    public int getList(int[] output) {
        Node tmp=head;
        int index=0;
        while(tmp.next!=null)
        {
            tmp=tmp.next;
            output[index]=tmp.data;
            index+=1;
        }
        return index;
    }
}