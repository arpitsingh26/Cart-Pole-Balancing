# Brief description of INAC and What it does:

Incremental Natural Actor Critic (INAC) algorithm is a variant of Actor Critic
algorithm in which the weight vector w is used which is incrementally updated
and used as an estimate of the natural gradient to update the actor weights.
In the actor critic algorithm, the actor stores the policy while the critic cri-
tiques the actions chosen by the actor by computing the corresponding value
function.

The state values are estimated by calculation of v T φ(s). The critic weights
v are updated with TD(λ) after which the policy weights θ of the actor are up-
dated based on the TD error δ and the eligibility trace e θ . In INAC algorithm,
we introduce weight vectors w also that get incrementally updated. They are
used for estimating the natural gradient in order to update the actor weights θ.
The algorithm uses the natural gradient G(u)^(−1)  Grad(u) J(π) where G(u) is the Fisher
information matrix.

# Pseudocode:

Please look in the attached report.
