class Singleton
  @instance = new

  private_class_method :new

 
  def self.instance
    @instance
  end

  
  def some_business_logic
    # ...
  end
end

#Codigo de cliente

s1 = Singleton.instance
s2 = Singleton.instance

if s1.equal?(s2)
  print 'Sngleton, funciona ambas variables con la misma intancia.'
else
  print 'Erros, singleton funciona con distintas instancias.'
end