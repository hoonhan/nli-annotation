import axios from 'axios'


export default {
    server_call(self, fn, url) {
        axios.get(self.$store.state.server_url + url, {
          params: {
            mturk_id: self.$store.state.mturk_id
          }
        }).then(function (res) {
          fn.apply(this, [self, res])
        }).catch(function(err) {
          alert("Server is not responding\n" + err);
        });
    },
    isWrongAccess(self) {
      if (self.$store.state.mturk_id === null) {
        alert("You should register your mturk ID to proceed to the task.\n")
        self.$store.commit('reset_mturk_id')
        self.$router.push('/')
      }
    }
};