# RoleOfLuckInSuccess

## Data Sampling

> **_NOTE:_** Every value mentioned below is configurable with the code change.

We have taken 20,000 persons participated in a contest which has score value from 1 to 100. Each person is assigned a random score from [1, 100]. Then, their score has been modified with the luck contribution (random luck value from [1, 100]) at different percentages.

Now, we have selected top 10 highest scoring people. Then, we have again selected top 10 highest scoring people based on the pure skill (after removing their luck value from total score). We check how many people have been remained in top 10 after removing the luck score.

We have repeated this process 1000 times to iron out the randomness bias.

## Result

We have found that on an average ~1 out of 10 people retain their spot in top 10 after their luck removed.