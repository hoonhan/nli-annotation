<template>
<div>
  <h1> Instruction </h1>
  Given a sentence(so-called premise), you should write a sentence that matches a specific class type.
  In total, you should write three sentences for the same premise, one for each of the following class types.<br><br>

  <ul>
  <li> <v-chip color="primary" class="ma-2" label>entailment</v-chip> : Write a sentence that is <b>definitely true</b> regarding the premise.</li>
  <li> <v-chip color="green" class="ma-2" label>neutral</v-chip> : Write a sentence that <b>might be true</b> regarding the premise.</li>
  <li> <v-chip color="pink" class="ma-2" label>contradiction</v-chip>: Write a sentence that is <b>definitely false</b> regarding the premise.</li>
  </ul><br>

  <h3> Notes </h3>
  <ul>
  <li> Premises are a caption of one photo. </li>
  <li> When writing sentences, you can use what you know about the world. </li>
  <li> Your sentences should <b>NOT</b> sound absurd regarding the premise.</li>
  </ul><br> 

  <h3> Examples </h3>
  Assume that a premiseㅤ<span class="amplf">John is taking a nap on the sofa.</span>ㅤis provided.
  <ul>
  <li> An example ofㅤ<v-chip color="primary" class="ma-2" label>entailment</v-chip>ㅤcan beㅤ<span class="amplf">John is sleeping.</span>ㅤbecause he is definitely sleeping.</li>
  <li> However,ㅤ<span class="amplf">The sun rises everyday </span>ㅤis not an appropriate response for entailment class since the statement is true regardless of the premise.</li><br>
  <li> An example ofㅤ<v-chip color="green" class="ma-2" label>neutral</v-chip>ㅤcan beㅤ<span class="amplf">John is snoring.</span>ㅤbecause he may or may not snore.</li>
  <li> However,ㅤ<span class="amplf">Bob is running on the ground</span>ㅤis not an appropriate response for neutral class since the statement does not share any context with the premise, thus sounds too absurd.</li><br>
  <li> An example ofㅤ<v-chip color="pink" class="ma-2" label>contradiction</v-chip>ㅤcan beㅤ<span class="amplf">John is playing soccer with Bob.</span>ㅤbecause the statement cannot be true while John is asleep.</li>
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