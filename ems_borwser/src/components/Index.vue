    <template>
    <div id="wrap">
        <div id="top_content">
            <div id="header">
                <div id="rightheader">
                    <p>
                        2009/11/20
                        <br/>
                        <a href="javascript:;" @click="user_logout">安全退出</a>
                    </p>
                </div>
                <div id="topheader">
                    <h1 id="title">
                        <a href="#">main</a>
                    </h1>
                </div>
                <div id="navigation">
                </div>
            </div>
            <div id="content">
                <p id="whereami">
                </p>
                <h1>{{admin_name}},欢迎您访问百知教育管理系统!!</h1>
                <table class="table">
                    <tr class="table_header">
                        <td>ID</td>
                        <td>Name</td>
                        <td>Photo</td>
                        <td>Salary</td>
                        <td>Age</td>
                        <td>Operation</td>
                    </tr>
                    <tr class="row1" v-for="(emp,i) in JSON.parse(emplist)":key="i">
                        <td>{{i+1}}</td>
                        <td>{{emp.emp_name}}</td>
                        <td><img style="height: 60px;" v-bind:src="src"></td>
                        <td>{{emp.salary}}</td>
                        <td>{{emp.age}}</td>
                        <td><a href="javascript:;" @click="del(emp.id)" >delete emp</a>&nbsp;| <a href="">update emp</a></td>
                    </tr>

                </table>
                <p>
                    <input type="button" class="button" value="Add Employee"/>
                </p>
            </div>
        </div>
        <div id="footer">
            <div id="footer_bg">
                ABC@126.com
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: "Index",
        data() {
            return {
                admin_name: '',
                emplist:[],
                src:'',
                id:'',
            }
        },
        methods: {
            del(i) {
                this.$axios({
                    url: "http://127.0.0.1:8000/api/users/",
                    method: "delete",
                    params:{
                        id:i,
                    }
                }).then(res => {
                    if (res.data) {
                      this.$message.success("删除成功")
                  } else {
                         this.$message.error("删除失败")
                    }
                }).catch(error=>{
                    console.log(error)
                    this.$message.error("删除失败")
                })
            },
            user_logout() {
                sessionStorage.removeItem("id")
                sessionStorage.removeItem("name")
                // 删除成功则跳转到首页
                this.$router.push("/login")
            },
            // 获取员工列表数据
            get_emp_list() {
                this.$axios({
                    url: "http://127.0.0.1:8000/emp/employees/",
                    method: "get",
                }).then(res => {
                    if (res.data) {
                        // 将用户的信息保存至 sessionStorage  用于展示用户信息
                        sessionStorage.emp = JSON.stringify(res.data)
                        this.emplist = sessionStorage.emp;

                        console.log(typeof(this.emplist)[0])
                    } else {
                        this.$message.error("错误")
                    }
                }).catch(error => {
                    console.log(error);
                    this.$message.error("错误")
                })
            },
         },
        // 在加载组件前判断用户是否登录，登录可以访问，未登录不能访问
        created() {
            let id = sessionStorage.id;
            if (id) {
                this.admin_name = sessionStorage.name;
            } else {
                this.$message.error("对不起，您还未登录，请登录后在访问");
                this.$router.push("/login");
            }

            // 调用获取员工列表数据的方法
            this.get_emp_list()

        },
    }
</script>

<style scoped>

</style>
