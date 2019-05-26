<template>
    <div class="card border-primary mt-1">
        <div class="card-header"> Listar amigos </div>
        <div class="card-body text-primary">
            <div class="alert alert-success" role="alert" v-if="status == 201">
                Se agrego exitosamente...
            </div>
            <div class="alert alert-success" role="alert" v-if="status == 200">
                Se actualizo exitosamente...
            </div>
            <form class="form-inline" role= "form" method="POST">
                <label class="my-1 mr-2"> Buscar por: </label>
                <select class="custom-select my-1 mr-sm-2" name="atributo">
                    <option v-for="item in fields" v-bind:value="item.field.toLowerCase()"> {{ item.field }} </option>
                </select>
                <input type="text" class="form-control mr-sm-2" placeholder="Escribir aqui.." name="valor" required>
                <button type="submit" class="btn btn-primary my-1"> Buscar </button>
                <router-link :to="{name: 'ListFriends', params: {status: 0}}" class="pl-2"> Listar </router-link>
                <!-- <a class="pl-2" href="/friends"> Todos </a> -->
            </form>
            <div class="table-responsive">
                <table class="table table-striped table-hover">
                    <thead>
                        <tr>
                            <th scope="col"> # </th>
                            <th scope="col" v-for="item in fields">
                                {{ item.field }}
                            </th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="(item, index) in friends">
                            <td> {{ index + 1 }} </td>
                            <td> {{ item.first_name }} </td>
                            <td> {{ item.last_name }} </td>
                            <td> {{ item.phone }} </td>
                            <td> {{ item.address }} </td>
                            <td> {{ item.birthday }} </td>
                            <td>
                                <router-link :to="{name: 'UpdateFriend', params: {id: item.id}}" class="text-info" data-toggle="tooltip" data-placement="bottom" title="Editar"> <i class='fas fa-edit'></i> </router-link>
                                <!-- <a href="/friend/23/" class="text-info" data-toggle="tooltip" data-placement="bottom" title="Editar"> <i class='fas fa-edit'></i> </a> -->
                                <!-- <a href="eliminar.php?id= <?= $fila['id'] ?>" class="text-danger" onClick="return confirm('Estas seguro?');" data-toggle="tooltip" data-placement="bottom" title="Eliminar"> <i class='fas fa-trash'></i> </a> -->
                                <router-link :to="{name: 'DeleteFriend', params: {id: item.id}}" class="text-danger" data-toggle="tooltip" data-placement="bottom" title="Eliminar"> <i class='fas fa-trash'></i> </router-link>
                            </td>
                        </tr>
                    </tbody>
                </table>
                <!-- <nav aria-label="Page navigation example">
                    <ul class="pagination justify-content-center">
                        <li class="page-item <?= $_GET['pagina'] <= 1 ? 'disabled': '' ?>">
                            <a class="page-link" href="listar.php?pagina=<?= $_GET['pagina'] - 1 ?>" tabindex="-1" aria-disabled="true"> Anterior </a>
                        </li>
                        <?php 
                            for ($i = 1; $i <= $paginas; $i++) { 
                        ?>
                                <li class="page-item <?= $_GET['pagina'] == $i ? 'active': '' ?>"><a class="page-link" href="listar.php?pagina=<?= $i ?>"> <?= $i ?> </a></li>
                        <?php 
                            }
                        ?>
                        <li class="page-item <?= $_GET['pagina'] >= $paginas ? 'disabled': '' ?>">
                            <a class="page-link" href="listar.php?pagina=<?= $_GET['pagina'] + 1 ?>"> Siguiente </a>
                        </li>
                    </ul>
                </nav> -->
            </div>
        </div>
    </div>
</template>

<script>
    import axios from "axios"

    export default {
        data () {
            return {
                status: this.$route.params.status,
                fields: [
                    {field: "Nombres"},
                    {field: "Apellidos"},
                    {field: "Teléfono"},
                    {field: "Dirección"},
                    {field: "Cumpleaños"},
                    {field: "Acciones"}
                ],
                friends: []
            }
        },
        methods: {
            getFriends () {
                const url = `${process.env.BASE_URL}/friends/`
                axios.get(url).then((response) => {
                    this.friends = response.data
                })
                .catch((err) => {
                    console.log(err)
                })
            }
        },
        created () {
            this.getFriends()
            // $('[data-toggle="tooltip"]').tooltip()
        }
    }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
    
</style>
