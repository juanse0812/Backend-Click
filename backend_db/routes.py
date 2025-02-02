from controllers import LoginUserControllers, RegisterUserControllers, Productos,app, PedidosUserControllers,ReservarUserControllers, DatosEmpresa, ProductosEmpresa, DatosEmpresaId
from controllers import updateProduct, delete, EnviarProductos, PedidosUser, agregar, Pedido,RegisterEmpresaControllers, MostrarNegocios, MostrarNegocioId, RegisterEmpresaControllers, ActualizarNegocio, EliminarNegocio, MostrarProductosNegocio, ProductoId, CrearProducto, ActualizarProducto, EliminarProducto, MostrarTodosLosNegocios, MostrarNegocio



user = {
    "pedido_user": "/api/v01/pedido", "pedido_user_controllers":  Pedido.as_view("pedido_api"),

    "login_user": "/api/v01/user/login", "login_user_controllers": LoginUserControllers.as_view("login_user"),

    "data_empresa": "/api/v01/user/datosempresa", "data_empresa_controllers": DatosEmpresa.as_view("data_empresa"),
    "data_empresa_id": "/api/v01/user/datosempresaid", "data_empresa_id_controllers": DatosEmpresaId.as_view("data_empresa_id"),
    
    "producto_empresa": "/api/v01/user/productoempresa", "producto_empresa_controllers": ProductosEmpresa.as_view("producto_empresa"),
    "enviar_productos":"/api/v01/user/enviarproductos", "enviar_productos_controllers":EnviarProductos.as_view("enviar_productos"),
    
    "registro_user": "/api/v01/user/registro", "user_registro_controllers": RegisterUserControllers.as_view("registro_user"),
    
    "Productos_clients":"/api/v01/user/product","productos":Productos.as_view("productos_api"),
    "Productos_clients_pedidos":"/api/v01/user/getInfo","productosPedidos":PedidosUserControllers.as_view("pedidos"),
    "Reservar_user":"/api/v01/user/reservar","reservar_user_controllers":ReservarUserControllers.as_view("reservar_api"),
    "PedidosUser":"/api/v01/user/pedido","pedidosUsers":PedidosUser.as_view("api_pedidos"),
    "ActualizarProducto":"/api/v02/user/updateProduct","update":updateProduct.as_view('update_product'),
    "delenteProduct":"/api/v02/user/deleteProduct","Productdelete":delete.as_view("delenteProduct_api"),
    "AgregarProduct":"/api/v02/user/agregar","insertProduct":agregar.as_view("agregar_api"),

    #modulo negocio
    "mostrar_todos_negocios":"/api/v02/user/negocios","negocios":MostrarTodosLosNegocios.as_view("negocios_api"),
    "mostrar_negocios":"/api/v02/user/mostrarNegocios","mostrarNegocios":MostrarNegocios.as_view("mostrar_negocios_api"),
    "mostrar_negocio":"/api/v02/user/negocio","negocio":MostrarNegocio.as_view("negocio_api"),
    "register_empresa": "/api/v01/user/registerEmpresa","registerEmpresa_controllers": RegisterEmpresaControllers.as_view("registerEmpresa_api"),
    "mostrar_negocio_id":"/api/v02/user/mostrarNegocioId","mostrarNegocioId":MostrarNegocioId.as_view("mostrar_negocio_id_api"),
    "actualizar_negocio":"/api/v02/user/actualizarNegocio","actualizarNegocio":ActualizarNegocio.as_view("actualizar_negocio_api"),
    "eliminar_negocio":"/api/v02/user/eliminarNegocio","eliminarNegocio":EliminarNegocio.as_view("eliminar_negocio_api"),
    
    #modulo producto
    "mostrar_productos":"/api/v02/user/mostrarProductos","mostrarProductos":MostrarProductosNegocio.as_view("mostrar_productos_api"),
    "producto_id":"/api/v02/user/productoId","productoId":ProductoId.as_view("producto_id_api"),
    "crear_producto":"/api/v02/user/crearProducto","crearProducto":CrearProducto.as_view("crear_producto_api"),
    "actualizar_producto":"/api/v02/user/actualizarProducto","actualizarProducto":ActualizarProducto.as_view("actualizar_producto_api"),
    "eliminar_producto":"/api/v02/user/eliminarProducto","eliminarProducto":EliminarProducto.as_view("eliminar_producto_api")

}
