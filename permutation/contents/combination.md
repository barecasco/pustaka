## I.  Combination Formula Derivation

### Combination: Inquire (1)

- Now we have a new kind of set. The set of 6 Infinity Stones: {space, time, mind, power, soul, reality}.

- These stones are spread across the universe. As ambitious as you might be, you just want to obtain any 3 of them.

- If you want to obtain any 3 of the 6 stones, it means you don't care which stones you get and the order of getting them.

- Now, you don't want to create a sequence of 3 stones. You want a **set** of 3 stones.

- How many possibilities of set that you can obtain? Let us use our raw brain power to see the possibilities.

### Combination: Inquire (2)
To compute the possible sets, you have to make sure that no two or more sets are "clones". Ex: {space, time, mind} and {time, space, mind} ARE clones to each other because the order of the members of a set can be arbitrary.

### Combination: Inquire (3)
- There are only 20 unique sets possible!
- We just did what is called finding **combination** of 3 from 6 Infinity Stones.
- If you ask why the word "combination", change the Infinity Stones set to ice cream toppings and see if the word makes sense to you.

- How many possible sets if you want all of the 6 stones? One :)

### Combination: Deriving the Formula (1)
- The 20 possible sets are also the members of the permutation sequences $$P(6,3)=120$$ of the Stones.
- The idea is how to get rid of other members in the permutation sequences so only the 20 sequences that represent the combination remain.

### Combination: Deriving the Formula (2)

- Assume all of the $$120$$ permutation sequences are sets. Now we have $$120$$ sets, where each set has 3 members.
- Each set has permutation of $$P(3,3)=6$$ sequences that are also members of the 120 sets we have.
- This 6 sequences differs only in order, which makes them clones if they are assumed as sets. Let us call this 6 sets a clone group.
- Our 120 sets consist of clone groups, where each group consists of 6 sets. That means we have $$120/6=20$$ clone groups.
- If we merge every clone group as only 1 set, now we have 20 unique sets.

### Combination: Deriving the Formula (3)
- Start by calculating the number of permutation sequences from the set:

$$
P(n, k)=\frac{n!}{(n-k)!}
$$

- Based on the previous slide, the combination number $$C(n,k)$$ is calculated by dividing the permutation number $$P(n,k)$$ by the permutation number of the members of the picked set, $$k!$$.

$$
\boxed{
    \begin{aligned}
    \\ ~~~~ C(n, k)=\,\frac{n!}{k!(n-k)!} ~~~~ \\\\
    \end{aligned}
}
$$
