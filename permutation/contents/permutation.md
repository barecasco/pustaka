## I.  Permutation Formula Derivation

### Permutation: Inquire (1)
- Let {a, b, c, d, e} a set of 5 letters that you want to play with.

- You can create a sequence of 5 letters by taking out the letters blindfolded one by one e.g. [b, c, d, a, e].

- How many sequences you can create? The order of the letters of course matters! the sequence [e, d, c, b, a] is different from [a, b, c, d, e].

- Set up an imaginary jar containing the letters. You are going to pick the letters one by one.

### Permutation: Inquire (2)

- Pick the first letter from the jar. Can you guess the letter you will get? No. But you can tell there are 5 possibilities: "a", "b", "c", "d" or "e".

- What are the possibilities of the second letter? It depends on the first letter you get! If you get "c" for the first, the second will be "a", "b", "d", or "e".

- Whichever letter you get in the first pick, the number of possibilities of the second pick is always 4.

- The number of the possibilities of the third, the fourth and the fifth pick is 3, 2, and 1 respectively.

### Permutation: Calculating Possible Outcomes
- In the first pick, you have 5 possibilities.

- In the second pick, you have 4 possibilities for each possibility from the first pick. Up to two picks, you can say there are $$5 \times 4 = 20$$ different outcomes exist: ["a", "b"], ["a", "c"], ["a", "d"], ["a", "e"], ["b", "a"], ["b", "c"] ....

- The third pick has 3 possibilities for each outcome of the second pick. This gives $$5 \times 4 \times 3=60$$ different outcomes in three picks.

- Now we can calculate the total outcomes of five picks: $$5 \times 4 \times 3 \times 2 \times 1 = 120$$ different outcomes.

### Permutation: Deriving the Formula (1)
Let $$n!=n\times(n-1)\times(n-2)\times ... \times1$$, with $$0!=1$$. The number possibilities of our first case above is $$5!=120$$.


### Permutation: Deriving the Formula (2)

- To blindfoldedly picks $$n$$ letters from $$n$$-letters set to create a sequence is called **permutation** of $$n$$ letters.

- The permutation of $$n$$-letters set has $$n!$$ different outcomes.

- What if we want to permute only $$k$$ letters from the $$n$$-letters set? $$(k<n)$$

- Let us call the number of the possibilities from the permutation as $$P(n, k)$$.

### Permutation: Deriving the Formula (3)
- Permutation of $$k$$ letters from the $$n$$-letters set is the same as our first example except that the picking stops at the $$k$$-th pick. Ex: if $$k=3$$ and $$n=7$$ then $$P(7,3)=7\times6\times5=210$$ possibilities.

- We can formulate: $$P(n,k)=n\times(n-1)\times(n-2)\times ... \times (n-k+1)$$

- And let
$$n! = n\times(n-1)\times(n-2)\times ... \times(n-k+1) \times(n-k)\times ... \times1$$

- The idea is to get $$P(n,k)$$ from $$n!$$ above.

### Permutation: Deriving the Formula (4)
$$
\begin{equation*}
n! =\, \underbrace{n\times(n-1)\times(n-2)\times \dots\times(n-k+1)}_{P(n, k)} \times
\overbrace{(n-k)\times\dots\times1}^{(n-k)!}
\end{equation*}
$$

$$
    \boxed{
        \begin{aligned}
        \\ ~~~~ P(n, k)=\frac{n!}{(n-k)!} ~~~~ \\\\
        \end{aligned}
    }
$$
