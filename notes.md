# Measures realised return distribution vs long-run compounded wealth

## Terminology

Arithmetric return: $E[R]$, or the arithmetic average of periodic returns.

Geometric growth / compound growth rate: based on compounding across periods.

Log growth rate / continuously compounded growth rate: $E[\ln(1+R)]$


## Arithmetic return vs Geometric growth

Suppose your one-period simple return is $R$. The arithmetic expected return is simply

$$
\mu = E[R]
$$

This tells us the expected return over a single period of measurment. However, it does not tell us the rate at which wealth compounds over time.

Wealth evolves as 

$$
W_{t+1} = W_t(1 + R_t)
$$

Over many periods,

$$
\frac{W_T}{W_0} = \prod_{t=1}^{T}(1 + R_t)
$$

where $R_t$ is compounded per period. Taking the natural log on both sides,

$$
\ln\left(\frac{W_T}{W_0}\right)
=
\ln(1+R_{0,T})
=
\sum_{t=1}^{T}\ln(1+R_t)
$$

Log returns over a horizon is just the sum of the log returns of each period in the horizon.

## Continuously compounded growth rate

Suppose we want to describe wealth growing at some continuously compounded rate $g$.

$$
W_T = W_0 e^{g_T T}
$$

Dividing $W_T$ by $W_0$ and taking the natural logs of both sides,

$$
\ln\left(\frac{W_T}{W_0}\right)
=
\ln(1+R_{0,T})
=
g_TT
$$

Therefore,

$$ g_TT
= 
\sum_{t=1}^{T}\ln(1+R_t)
$$
$$
g_T = \frac{1}{T}\sum_{t=1}^{T}\ln(1+R_t)
$$

Here, $g_T$ and $R_t$ are random variables before returns are realised. Taking Expectations of the expression for $g_T$,

$$
E[g_T]
=
\frac{1}{T}\sum_{t=1}^{T}E[\ln(1+R_t)]
$$
If the $R_t$'s are i.i.d., then
$$
E[g_T] \equiv g = E[\ln(1+R)] 
$$

Here, $g$ is the *expected* continuously compounded growth rate implied by the distribution of the simple return $R$.


In contrast, $g_T$ is the realized continuously compounded growth rate over (T) periods, based on the realized returns $R_1,\ldots,R_T$.

## $g$ vs $g_t$

$$
g_T = \frac{1}{T}\sum_{t=1}^{T}\ln(1+R_t)
$$

is a random realised sample continuously compounded growth rate over T periods.

Whereas,

$$
g \equiv E[g_T]= E[\ln(1+R)] 
$$

is the expected continuously compounded growth rate.

Different possible return paths gives different $g_T$'s

$$
g_T^{(1)},\; g_T^{(2)},\; g_T^{(3)},\; \ldots
$$

and $g$ is the average or *expectation* of those outcomes

$$
g = E[g_T]
$$

If the $R_t$'s are identically distributed,

$$
E[g_T]
=
E[\frac{1}{T}\sum_{t=1}^{T}\ln(1+R_t)]
=
\frac{1}{T}\sum_{t=1}^{T}E[\ln(1+R_t)]
=
E[\ln(1+R)]
$$

$g_T$ is the realised continuous compounded growth rate per period whereas $g$ is the *expected* continuous compounded growth rate per period.

If our period of measurement is 1 day then $g$ is the expected continuously compounded growth rate per day.

## $g_T$ tends to $g$ as T gets large

$g_T$ is an average of many log returns.

$$
g_T = \frac{1}{T}\sum_{t=1}^{T}\ln(1+R_t)
$$

Let $X_t = \ln(1+R_t)$ Then,

$$
g_T = \frac{1}{T}\sum_{t=1}^{T}X_t
$$

Via the Law of Large Numbers,

$$
\lim_{T \to \infty}
\frac{1}{T}\sum_{t=1}^{T} X_t
=
E[X]
$$

So,

$$
\lim_{T \to \infty}
\frac{1}{T}\sum_{t=1}^{T} \ln(1+R_t)
=
E[\ln(1+R_t)]
= 
g
$$

$$
g_T \to g
\quad \text{as } T \to \infty
$$

Useful analogy: propotion of heads to tails for a fair coin repeatedly flipped as the number of flips gets larger and larger. At the start,$\frac{No. Heads}{No. Tails}$ might have deviated significantly from 0.5 but as the coin is flipped more and more times, the ratio will tend to 0.5. 
## Arithmetic growth rate vs Expected continuously compounded growth rate
Over the same period,

Arithmetic expected return: $E[R]$

Expected log growth: $E[\ln(1+R)]$