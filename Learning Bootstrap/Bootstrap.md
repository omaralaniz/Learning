# bootstrap

## Grid

```html
<div class="container my-container">
        <div class="row my-row">
            <!--The col max is 12 but it can be less than 12-->
            <div class="col-md-4 col-sm-6 my-col">
                row 1 col 1
            </div>
            <div class="col-md-8 col-sm-6 my-col">
                    row 1 col 2
            </div>
        </div>
        <div class="row justify-content-between align-items-stretch my-row">
            <div class="col-4 offset-2 my-col order-md-12">
                row 2 col 1
            </div>
            <div class="col-4 align-self-start my-col order-md-2">
                    row 2 col 2
            </div>
        </div>
    </div>
```

## Alerts & Modal

```html
 <div class="modal fade" id="myConfirmModal">
            <div class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-header">
                        <h2 class="modal-title">Please Confirm</h2>
                        <button type="button" class="close" data-dismiss="modal"><span>&times;</span></button>
                    </div>
                    <div class="modal-body">
                        <p>This is the modal body, od you like it?</p>
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-secondary" data-dismiss="modal">Confirm</button>
                    </div>
                </div>
            </div>
        </div>



<div class="container">
    <div class="row">
        <div class="col">
            <h1>Alerts & Modal</h1>
        </div>
    </div>

    <div class="row">
        <div class="col">
            <div class="alert alert-success alert-dismissible fade show" role="alert">
                <button type="button" class="close" data-dismiss="alert"><span aria-hidden="true">&times;</span></button>
                <h2 class="alert-heading">This is an alert!</h2>
                <p>ES AN ALERT
                    <a href="#" class="alert-link">Click ME!</a>
                </p> 
                
            </div>
        </div>
    </div>
    <div class="row">
        <div class="col">
            <button type="button" class="btn btn-primary" data-toggle="modal"data-target="#myConfirmModal">Show Modal</button>
        </div>
    </div>
</div>
```

