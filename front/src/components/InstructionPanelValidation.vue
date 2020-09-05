<template>
<div>
  <h1> Instruction </h1>
  Given a pair of sentences, <b>premise</b> and <b>hypothesis</b>, you should choose one of the labels that best describes the logical relationship of them.

  <ul>
  <li> <v-chip color="primary" class="ma-2" label>entailment</v-chip>: The hypothesis is <b>definitely true</b> regarding the premise.</li>
  <li> <v-chip color="green" class="ma-2" label dark>neutral</v-chip>: The hypothesis <b>might be true</b> regarding the premise.</li>
  <li> <v-chip color="pink" class="ma-2" label dark>contradiction</v-chip>: The hypothesis is <b>definitely false</b> regarding the premise.</li>
  </ul><br>

  In addition, you can choose <v-chip color="grey" class="ma-2" label dark>inappropriate</v-chip> if two sentences do not share the same context or situation. i.e., when the hypothesis sounds absurd regarding the premise. 
  
  <br><br>

  <h3> Examples </h3>
  Assume that a premiseㅤ<span class="amplf">John is taking a nap on the sofa.</span>ㅤis provided. Then these hypotheses should be labeled as follows.
  <ul>
  <li> <span class="amplf">John is sleeping.</span>ㅤshould be labeled <v-chip color="primary" class="ma-2" label>entailment</v-chip> </li>
  <li> <span class="amplf">John is snoaring.</span>ㅤshould be labeled <v-chip color="green" class="ma-2" label dark>neutral</v-chip>ㅤbecause he may or may not snore.</li>
  <li> <span class="amplf">John is playing soccer with Bob.</span>ㅤshould be labeled <v-chip color="pink" class="ma-2" label dark>contradiction</v-chip>ㅤbecause the statement cannot be true while John is asleep.</li>
  <li> <span class="amplf">The sun rises everyday.</span>ㅤshould be labeled <v-chip color="grey" class="ma-2" label dark>inappropriate</v-chip>  since the statement is true regardless of the premise.</li>
  <li> <span class="amplf">Bob is running on the ground.</span>ㅤshould be labeled <v-chip color="grey" class="ma-2" label dark>inappropriate</v-chip>ㅤsince the statement does not share any context with the premise, thus sounds too absurd.</li>
  </ul><br>
</div>
</template>

<style scoped>
.v-chip {
  margin: 0!important;
}

.amplf {
  font-style: italic;
  font-weight: bold;
  color: #1a75ff;

}
</style>