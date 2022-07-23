package DayTwo.swea13501;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

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

class Solution {

    private static BufferedReader br;
    private final static int MAX_NODE = 10000;

    private static Node[] node = new Node[MAX_NODE];
    private static int nodeCnt = 0;
    private static Node head;
    private static int []output=new int[MAX_NODE];

    public static Node getNode(int data) {
        node[nodeCnt] = new Node(data);
        return node[nodeCnt++];
    }

    public static void init() {
        head=new Node();
    }

    public static void addNode2Tail(int data) {
        Node new_node=getNode(data);
        Node tmp=head;
        while(tmp.next!=null){
            tmp=tmp.next;
        }
        tmp.next=new_node;
    }

    public static void addNode2Num(int data, int num) {
        int index=0;
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
    public static void changeNum(int index, int change_num){
        int i=0;
        Node tmp=head;
        while(i<=index){
            tmp=tmp.next;
            i+=1;
        }
        tmp.data=change_num;
    }
    public static void removeNode(int index) {
        int i=0;
        Node tmp=head;
        Node tmp2=head.next;
        while(i<index){
            tmp=tmp.next;
            tmp2=tmp2.next;
            if(tmp2.next==null){
                break;
            }
            i+=1;
        }
        tmp.next = tmp2.next;
    }
    public static int getList(int[] output) {
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
    public static int solution(int M,int L) throws Exception{
        StringTokenizer order;
        String cmd;
        int index,add_num,change_num,ret;
        for(int i=0;i<M;i++){
            String orders=br.readLine();
            order=new StringTokenizer(orders," ");
            cmd=order.nextToken();
            index=Integer.parseInt(order.nextToken());
            switch(cmd){
                case "I":
                    add_num=Integer.parseInt(order.nextToken());
                    addNode2Num(add_num,index);
                    break;
                case "D":
                    removeNode(index);
                    break;
                case "C":
                    change_num=Integer.parseInt(order.nextToken());
                    changeNum(index,change_num);
                    break;
            }
        }
        ret = getList(output);
        if(ret<L){
            return -1;
        }
        else{
            return output[L];
        }
    }
    public static void main(String args[]) throws Exception{
        int TC;
        int N,M,L;
        int num;
        int []arr;
        int ret;
        StringTokenizer st;
        StringTokenizer str_num;
        br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();
        TC = Integer.parseInt(str);

        for(int i=1;i<=TC;i++){
            str = br.readLine();
            st = new StringTokenizer(str, " ");
            N = Integer.parseInt(st.nextToken()); //수열의 길이
            M = Integer.parseInt(st.nextToken()); //추가횟수
            L = Integer.parseInt(st.nextToken()); //출력할 인덱스 번호

            init();

            String str_nums=br.readLine();
            str_num=new StringTokenizer(str_nums," ");

            for(int j=0;j<N;j++){
                num=Integer.parseInt(str_num.nextToken());
                addNode2Tail(num);
            }//Node에 잘 들어갔음.
            System.out.println("#"+i+" "+solution(M,L));
        }
    }
}
