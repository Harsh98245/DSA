class Solution {
    public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {

        int maxcandy=0;
        for (int i=0;i<candies.length;i++){
            if(candies[i]>maxcandy){
                maxcandy=candies[i];
            }
        }

           List<Boolean> result = new ArrayList<>(candies.length);

        for(int i =0 ; i< candies.length ; i++){
            if((candies[i]+ extraCandies) >= maxcandy ){
                result.add(true);
            }else{ result.add(false);}
           
        }
        return result;
    }
}