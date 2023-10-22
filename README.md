# RoleOfLuckInSuccess

## Data Sampling

> **_NOTE:_** Every value mentioned below is configurable with the code change.

We have taken 20,000 persons who participated in a contest which has a score value from 1 to 100. Each person is assigned a random score from [1, 100]. Then, their score has been modified with the luck contribution (random luck value from [1, 100]) at different percentages.

Now, we have selected the top 10 highest-scoring people. Then, we again selected the top 10 highest-scoring people based on pure skill (after removing their luck value from the total score). We check how many people have remained in the top 10 after removing the luck score.

We have repeated this process 1000 times to iron out the randomness bias.

## Result

We have found that on average ~1 out of 10 people retain their spot in the top 10 after their luck is removed.

| ![graph-with-zero-percent](https://github.com/iamblizzard/RoleOfLuckInSuccess/blob/main/assets/graph-with-zero-percent.png) | 
|:--:| 
| *In this graph we took the first percentage as zero. At 0% we can see all 10/10 people retained in the top 10.* |

| ![graph-without-zero-percent](https://github.com/iamblizzard/RoleOfLuckInSuccess/blob/main/assets/graph-without-zero-percent.png) | 
|:--:| 
| *In this graph we removed the zero percentage to show the data in more detail for non-zero percentages.* |