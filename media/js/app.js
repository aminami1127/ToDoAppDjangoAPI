$.ajaxPrefilter( function( options, originalOptions, jqXHR ) {
  options.url = 'http://127.0.0.1:8000/todo' + options.url;
});

$(document).ready(function(){

	var Task = Backbone.Model.extend({
    urlRoot: '/',
		defaults: {
			name: 'do something',
			completed: false,
			date: '2015-02-10'
		},
	  validate: function(attrs){
			if(_.isEmpty(attrs.name)){
				return 'Name must not be empty!';
			}
		},
	  initialize: function(){
			this.on("invalid", function(model, error){
				$('#error').html(error);
			});
		}
	});
	var Tasks = Backbone.Collection.extend({url: '/list/', model: Task});

	var TaskView = Backbone.View.extend({
		tagName: 'li',
	  initialize: function(){
			this.model.on('destroy', this.remove, this);
			this.model.on('change', this.render, this);
		},
	  events: {
			'click .delete': 'destroy',
			'click .toggle': 'change'
		},
	  destroy: function(){
			if(confirm('Are you sure?')){
				this.model.destroy();
			}
		},
	  remove: function(){
			this.$el.remove();
		},
	  change: function(){
			this.model.set('completed', !(this.model.get('completed')));
		},
	  template: _.template($('#task-template').html()),
		render: function(){
			var template = this.template(this.model.toJSON());
			this.$el.html(template);
			return this;
		}
	});

	var TasksView = Backbone.View.extend({
		tagName: 'ul',
	  initialize: function(){
			this.collection.on('add', this.addNew, this);
			this.collection.on('add', this.updateCount, this);
			this.collection.on('change', this.updateCount, this);
			this.collection.on('destroy', this.updateCount, this);
		},
	  addNew: function(task){
      task.url = '/list/';
      task.save();
			var taskView = new TaskView({model: task});
			this.$el.append(taskView.render().el);
			$('#name').val('').focus();
			return this;
		},
	  updateCount: function(){
			var uncompletedTasks = this.collection.filter(function(task){
				return !(task.get('completed'));
			});
			$('#count').html(uncompletedTasks.length);
		},
	  render: function(){
			this.collection.each(function(task) {
				var taskView = new TaskView({model: task});
				this.$el.append(taskView.render().el);
			}, this);
			this.updateCount();
			return this;
		}
	});

	var AddTaskView = Backbone.View.extend({
		el: '#addTask',
	    	events: {
			'submit': 'submit'
		},
	  submit: function(e){
			e.preventDefault();
			//var task = new Task({name: $('#name').val()})
			var task = new Task();
			if(task.set({name: $('#name').val()}, {validate: true})){
				this.collection.add(task);
				$('#error').empty();
			}
		}
	});

	var tasks = new Tasks();
  tasks.fetch({
    success: function(tasks) {
      var tasksView = new TasksView({collection: tasks});
      var addTaskView = new AddTaskView({collection: tasks});
      $('#tasks').html(tasksView.render().el);
    }
  })
});
