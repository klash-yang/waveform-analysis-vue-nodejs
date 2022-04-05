<template>
  <div class="layout-ceiling">
    <Dropdown style="float: right" placement="bottom-end">
      <Button type="text" style="margin-top: -3px; margin-right:-10px;">
        <Avatar class="avatar" shape="square"
                :src="user.imageUrl ? user.imageUrl : 'https://i.loli.net/2017/08/21/599a521472424.jpg'"/>
      </Button>
      <DropdownMenu slot="list">
        <DropdownItem @click.native="setProfile">Personal Setting</DropdownItem>
        <DropdownItem @click.native="logout" divided>Log out</DropdownItem>
      </DropdownMenu>

    </Dropdown>
    <div class="layout-ceiling-main align-middle">
      <a href="#/login">FII-IAI</a>
      <a href="#">Help</a>
      <a href="#">Info</a>
      <a href="#">Service</a>

    </div>


  </div>
</template>
<style scoped>
  .layout-ceiling {
    background: #464c5b;
    /*padding: 10px 0;*/
    height: 40px;
    overflow: hidden;
  }

  .layout-ceiling-main {
    float: right;
  }

  .layout-ceiling-main a {
    border-left: 1px solid #cccccc;
    color: #9ba7b5;
    padding: 0 10px;
    margin: 10px 0;
    text-align: center;
    cursor: pointer;
    font-size: 14px;
    line-height: 14px;
    position: relative;
  }

  .layout-ceiling-main a:hover {
    color: #fff;
  }

  .layout-ceiling .avatar {
    float: right;
    margin-right: 1em
  }
</style>
<script>
  import { mapGetters } from 'vuex'

  export default {
    name: 'ceiling',
    props: {
      itemList: Array
    },
    computed: mapGetters({
      user: 'userDetail'
    }),
    methods: {
      setProfile () {
        this.$router.push({path: '/profile'})
      },
      logout () {
        this.$store.dispatch('logout')
        this.$router.push({path: '/login'})
      }
    }
  }
</script>
