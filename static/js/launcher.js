class Launcher {
  constructor(){
    this.entries = $('a.entry');
    this.idx = 0;

    this.listener = new window.keypress.Listener();
    this.listener.register_many([
        {keys: 'right', on_keydown: this.next, this: this},
        {keys: 'left', on_keydown: this.prev, this: this},
        {keys: 'enter', on_keydown: this.launch, this: this}
    ]);

    this.focus();
  }

  next(){
    if (++this.idx >= this.entries.length){
      this.idx = 0;
    }

    this.focus();
  }

  prev(){
    if (--this.idx < 0){
      this.idx = this.entries.length - 1;
    }

    this.focus();
  }

  launch(){
    var entry = this.entries[this.idx];
    entry.click();
  }

  focus(){
    this.unfocus_all();
    var entry = this.entries[this.idx];
    $(entry).addClass('focused');
  }

  unfocus_all(){
    this.entries.each(function(i, e){
      $(e).removeClass('focused');
    });
  }
}

$(function(){
  new Launcher();
});

