<template>
  <div class="log-form">
    <Card :bordered="false">
      <p slot="title" style="text-align: center;">Login</p>
      <Form ref="loginForm" :model="loginForm" :rules="loginFormRule">
        <FormItem prop="username">
          <Input type="text" v-model="loginForm.username" placeholder="User name">
          <Icon type="ios-person-outline" slot="prepend"></Icon>
          </Input>
        </FormItem>
        <FormItem prop="password">
          <Input type="password" v-model="loginForm.password" placeholder="Password">
          <Icon type="ios-locked-outline" slot="prepend"></Icon>
          </Input>
        </FormItem>

        <div style="text-align: center">
          <Button type="primary" @click="handleSubmit('loginForm')">Login</Button>
          <Button type="ghost" style="margin-left: 8px">Cancel</Button>
        </div>
        <div style="padding: 20px">
          <span style="float: left">
            <Switch v-model="loginForm.rememberMe" @on-change="changeRememberMe"> </Switch>  Rememberme
          </span>
          <a class="forgot" href="#">Forget password?</a>
        </div>
      </Form>
    </Card>


  </div><!--end log form -->

</template>

<style rel="stylesheet/less" type="text/css" lang="less">

  @blue :#3399ff;
  .log-form {
    width: 350%;
    min-width: 320px;
    max-width: 450px;
    background: #fff;
    position: absolute;
    top: 50%;
    left: 50%;
    -webkit-transform: translate(-50%, -50%);
    -moz-transform: translate(-50%, -50%);
    -o-transform: translate(-50%, -50%);
    -ms-transform: translate(-50%, -50%);
    transform: translate(-50%, -50%);

    box-shadow: 0px 2px 5px rgba(0, 0, 0, .25);

  .forgot, .remember {
    color: lighten(@blue, 10%);
    float: right;

  &
  :hover {
    color: darken(@blue, 5%);
  }

  }
  }


</style>
<script>
  import user from '../api/user.api'

  export default {
    data () {
      return {
        loginForm: {
          'password': 'admin',
          'rememberMe': false,
          'username': 'admin'
        },
        loginFormRule: {
          username: [
            {required: true, message: 'Please input username', trigger: 'blur'}
          ],
          password: [
            {required: true, message: 'Please input password', trigger: 'blur'},
            {type: 'string', min: 3, message: 'password length should be no less than 3', trigger: 'blur'}
          ]
        }
      }
    },
    mounted () {
      if (localStorage.getItem('rememberMe') === 'true') {
        this.$set(this.loginForm, 'rememberMe', true)
      }else{
        this.$set(this.loginForm, 'rememberMe', false)

      }
      this.changeRememberMe() // trigger rememberMe
    },
    methods: {

      handleSubmit (name) {
        this.$refs[name].validate((valid) => {
          if (valid) {
            user.login(this.loginForm).then(res => {
              this.handleLoginSuccess(res)
            }).catch((error) => {
              this.handleLoginError(error)
            })

          }
        })
      },
      handleLoginSuccess: function (res) {
        this.$store.dispatch('initUser', res.data).then(() => {
          this.$Message.success('Login sucessfully')
          this.$router.push({
            name: 'home'
          })
        })
      },
      handleLoginError: function (error) {
        if (error && error.response
          && error.response.status === 401
          && error.response.data
          && error.response.data.AuthenticationException) {
          let authenticationException = error.response.data.AuthenticationException
          let msg = 'Username/Password incorrect'
          if (authenticationException === 'User user was not activated') {
            msg = 'user not activated'
          }
          this.$Message.error(msg)

        } else {
          if (error.response && error.response.data && error.response.data.message) {
            this.$Message.error(error.response.data.message)

          }
        }
      },
      changeRememberMe () {
        this.$store.dispatch('changeStorage', this.loginForm.rememberMe)
      }
    }
  }
</script>
