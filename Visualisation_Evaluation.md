# Visualisation Evaluation

The graphs in `titanic_visualisations.ipynb` were chosen using two criteria:

1. The variable shows evidence of influencing survival.
2. The variable is balanced between the train and test data, so patterns learned from the training set should carry over to the test set.

## Graphs included

**Sex.** This is the strongest predictor. Survival was 74% for women and 19% for men. The split is almost identical in train (35% female) and test (36% female), so it is both informative and reliable.

**Pclass.** Survival falls steadily with class: 63%, 47% and 24% for classes 1, 2 and 3. The class mix is similar in both sets (class 3 is 55% of train and 52% of test).

**Age interval.** Plotting survival against individual ages is too noisy. Many ages have only a handful of passengers, so survival jumps between 0% and 100% from one age to the next. Grouping ages into five intervals gives each bar enough passengers to be meaningful. The effect is smaller than for sex or class. Survival is roughly flat at 37–43% up to age 64, then drops to 9% for passengers aged 65 and over. That last group is small (11 passengers), so it should be read cautiously. One caveat is that passengers with no recorded age are placed in interval 0 with the children, which may dilute any child effect. The intervals are balanced between train and test.

**Fare.** The train vs test distribution is shown as a histogram, and the two sets have very similar medians (14.5) and quartiles. For the effect on survival, the fare interval proves more useful rather than the raw distribution, given the high variance of fares. Survival rises clearly across the four intervals, from 20% to 58%, and each interval holds about 25% of passengers in both sets.

**Age interval by Pclass.** This is the multivariate graph. It checks whether the age profile differs between classes, which matters because both class and age are strong drivers of survival. We can see across the age intervals, lower class passengers had higher rates of mortality and that mortality increases as age rises showing the strong combined effect of the two factors.

## Graphs excluded

**SibSp and Parch.** Roughly 68% of passengers have no siblings or spouses and about 76% have no parents or children. The other categories are tiny (some have a single passenger), so survival rates there are unstable. The balance between train and test is fine, but the groups are too small to draw conclusions from.

**Embarked.** The ports are less balanced across the datasets than other variables. Southampton is 72% of train but 65% of test, and Cherbourg is 19% against 24%. Port also overlaps with class, so it adds little beyond Pclass.

**Raw Age and Fare histograms split by survival.** These show the same information as the interval graphs, but with far more noise. The fare histogram is dominated by a long right tail, and the age histogram has the individual-age noise described above. The interval versions give a clearer picture.

**Fare interval train vs test, and Pclass by Fare Interval.** The first repeats the fare histogram. The second compares two variables that largely measure the same thing, since higher classes pay higher fares.

**Age interval by Embarked.** Since Embarked is excluded as a weak and unbalanced variable, a graph built on it would not help.
