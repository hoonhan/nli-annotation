<template>
<div>
  <div v-if="page===1">
  <h1> Instruction </h1>
  Given a sentence(so-called premise), you should write a sentence that matches a specific class type regarding one of the provided contexts.
  In total, you should write three sentences for the same premise, one for each of the following class types.<br><br>

  <ul>
  <li> <v-chip color="primary" class="ma-2" label>entailment</v-chip> : Write a sentence that is <b>definitely true</b> regarding the premise.</li>
  <li> <v-chip color="green" class="ma-2" label>neutral</v-chip> : Write a sentence that <b>might be true</b> regarding the premise.</li>
  <li> <v-chip color="pink" class="ma-2" label>contradiction</v-chip>: Write a sentence that is <b>definitely false</b> regarding the premise.</li>
  </ul><br>

  Additionally, we will provide you with the five context words for each premise sentence.<br><br>

  <ol>
  <li> For each class type, select one word among the context words and include it in the sentence you are writing.</li>
  <li> If all context words sound not relevant to the premise sentence, you can ask for new context words. The new context words may be more relevant to the premise than the previous words.</li>
  </ol><br>

  <b style="color:red;">>> Proceed to the next page.</b><br><br>

  </div>


  <div v-if="page===2">
  <h1> Instruction </h1>


  <h3> Notes </h3>
  <ul>
  <li> Your sentence should <b>NOT</b> sound absurd regarding the premise.</li>
  <li> The written sentence should make sense in itself.</li>
  <li> Context words are randomly selected from the English dictionary upon your request, so an inappropriate word can be selected.</li>
  </ul><br> 

  <h3> Examples </h3>
  Assume that a premiseㅤ<span class="amplf">John is taking a nap on the sofa</span>ㅤis provided.
  <ul>
  <li> With a context word <b>couch</b>, an example ofㅤ<v-chip color="primary" class="ma-2" label>entailment</v-chip>ㅤcan beㅤ<span class="amplf">John's hip is put on the couch</span></li>
  <li> However,ㅤ<span class="amplf">The sun rises everyday </span>ㅤis not an appropriate response for entailment class since the statement is true regardless of the premise. It does not include the context word as well.</li>
  <li> Also,ㅤ<span class="amplf">The couch is smiling, seeing John's face. </span>ㅤis not an appropriate response since the statement does not make sense.</li><br>
  <li> With a context word <b>grass</b>, an example ofㅤ<v-chip color="green" class="ma-2" label>neutral</v-chip>ㅤcan beㅤ<span class="amplf">John is dreaming that he is running around on the grass</span>ㅤbecause he may or may not dream.</li>
  <li> However,ㅤ<span class="amplf">Bob is running on the grass</span>ㅤis not an appropriate response for neutral class since the statement does not share any context with the premise, thus sounds too absurd.</li><br>
  <li> With a context word <b>soccer</b>, an example ofㅤ<v-chip color="pink" class="ma-2" label>contradiction</v-chip>ㅤcan beㅤ<span class="amplf">John is playing soccer with Bob</span>ㅤbecause the statement cannot be true while John is asleep.</li>
  </ul><br>
  </div>


  <v-divider/>
  <div style="bottom:0">
  <v-pagination
    v-model="page"
    :length="2"
  ></v-pagination>
  </div>
</div>
</template>

<script>
export default {
  data: () => {
    return {
      page: 1
    }
  }
}
</script>

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